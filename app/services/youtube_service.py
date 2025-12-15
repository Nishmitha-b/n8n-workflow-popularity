import requests
from app.utils.config import YOUTUBE_API_KEY

YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
YOUTUBE_VIDEO_URL = "https://www.googleapis.com/youtube/v3/videos"


def fetch_n8n_videos(region="US", max_results=5):
    # 1️⃣ Search for n8n workflow videos
    search_params = {
        "part": "snippet",
        "q": "n8n workflow",
        "type": "video",
        "regionCode": region,
        "maxResults": max_results,
        "key": YOUTUBE_API_KEY
    }

    search_response = requests.get(YOUTUBE_SEARCH_URL, params=search_params).json()

    video_ids = []
    for item in search_response.get("items", []):
        video_ids.append(item["id"]["videoId"])

    if not video_ids:
        return []

    # 2️⃣ Get video statistics
    stats_params = {
        "part": "statistics,snippet",
        "id": ",".join(video_ids),
        "key": YOUTUBE_API_KEY
    }

    stats_response = requests.get(YOUTUBE_VIDEO_URL, params=stats_params).json()

    workflows = []

    for video in stats_response.get("items", []):
        stats = video["statistics"]

        views = int(stats.get("viewCount", 0))
        likes = int(stats.get("likeCount", 0))
        comments = int(stats.get("commentCount", 0))

        workflows.append({
            "workflow": video["snippet"]["title"],
            "platform": "YouTube",
            "popularity_metrics": {
                "views": views,
                "likes": likes,
                "comments": comments,
                "like_to_view_ratio": round(likes / views, 4) if views else 0,
                "comment_to_view_ratio": round(comments / views, 4) if views else 0
            },
            "country": region
        })

    return workflows
