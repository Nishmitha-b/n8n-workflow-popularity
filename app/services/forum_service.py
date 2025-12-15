import requests

DISCOURSE_BASE_URL = "https://community.n8n.io"


def fetch_forum_workflows(limit=5):
    url = f"{DISCOURSE_BASE_URL}/latest.json"
    workflows = []

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        topics = data.get("topic_list", {}).get("topics", [])

        for topic in topics[:limit]:
            views = topic.get("views", 0)
            likes = topic.get("like_count", 0)
            replies = topic.get("reply_count", 0)
            contributors = topic.get("participants_count", 0)

            workflows.append({
                "workflow": topic.get("title", "Unknown"),
                "platform": "Forum",
                "popularity_metrics": {
                    "views": views,
                    "likes": likes,
                    "replies": replies,
                    "contributors": contributors,
                    "like_to_view_ratio": round(likes / views, 4) if views else 0,
                    "reply_to_view_ratio": round(replies / views, 4) if views else 0,
                    "contributor_to_view_ratio": round(contributors / views, 4) if views else 0
                },
                "country": "Global"
            })

    except Exception as e:
        print(f"Forum fetch failed: {e}")

    return workflows
