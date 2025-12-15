"""
Cron job entry point.
This script can be scheduled to run daily or weekly.
"""

from app.services.youtube_service import fetch_n8n_videos
from app.services.forum_service import fetch_forum_workflows
from app.services.google_service import fetch_google_trends


def run():
    print("Fetching YouTube data...")
    fetch_n8n_videos(region="US")
    fetch_n8n_videos(region="IN")

    print("Fetching Forum data...")
    fetch_forum_workflows()

    print("Fetching Google Trends...")
    fetch_google_trends(country="US")
    fetch_google_trends(country="IN")

    print("Data fetch completed.")


if __name__ == "__main__":"""
Cron job entry point.
This script can be scheduled to run daily or weekly.
"""

from app.services.youtube_service import fetch_n8n_videos
from app.services.forum_service import fetch_forum_workflows
from app.services.google_service import fetch_google_trends


def run():
    print("Fetching YouTube data...")
    fetch_n8n_videos(region="US")
    fetch_n8n_videos(region="IN")

    print("Fetching Forum data...")
    fetch_forum_workflows()

    print("Fetching Google Trends...")
    fetch_google_trends(country="US")
    fetch_google_trends(country="IN")

    print("Data fetch completed.")


if __name__ == "__main__":
    run()

   
