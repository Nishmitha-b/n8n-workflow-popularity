from fastapi import APIRouter, Query
from app.services.youtube_service import fetch_n8n_videos
from app.services.forum_service import fetch_forum_workflows
from app.services.google_service import fetch_google_trends

router = APIRouter()

@router.get("/workflows")
def get_workflows(
    platform: str = Query(default=None),
    country: str = Query(default=None)
):
    workflows = []

    # Normalize inputs
    platform = platform.lower() if platform else None
    country = country.upper() if country else None

    # ---- YOUTUBE ----
    if platform in (None, "youtube"):
        if country == "US":
            workflows.extend(fetch_n8n_videos(region="US", max_results=5))
        elif country == "IN":
            workflows.extend(fetch_n8n_videos(region="IN", max_results=5))
        else:
            workflows.extend(fetch_n8n_videos(region="US", max_results=5))
            workflows.extend(fetch_n8n_videos(region="IN", max_results=5))

    # ---- FORUM ----
    if platform in (None, "forum"):
        workflows.extend(fetch_forum_workflows(limit=5))

    # ---- GOOGLE ----
    if platform in (None, "google"):
        if country == "US":
            google_data = fetch_google_trends(country="US")
        elif country == "IN":
            google_data = fetch_google_trends(country="IN")
        else:
            google_data = (
                fetch_google_trends(country="US") +
                fetch_google_trends(country="IN")
            )

        # Only add if Google returned data
        if google_data:
            workflows.extend(google_data)

    return workflows
