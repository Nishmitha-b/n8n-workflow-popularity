from pytrends.request import TrendReq
from pytrends.exceptions import TooManyRequestsError


def fetch_google_trends(country="US"):
    pytrends = TrendReq(hl="en-US", tz=360)

    keywords = [
        "n8n workflow",
        "n8n automation",
        "n8n slack integration",
        "n8n gmail automation",
        "n8n whatsapp automation"
    ]

    workflows = []

    try:
        pytrends.build_payload(
            keywords,
            timeframe="today 3-m",
            geo=country
        )

        data = pytrends.interest_over_time()

        if data.empty:
            return workflows

        for keyword in keywords:
            avg_interest = int(data[keyword].mean())

            workflows.append({
                "workflow": keyword,
                "platform": "Google",
                "popularity_metrics": {
                    "average_search_interest": avg_interest
                },
                "country": country
            })

    except TooManyRequestsError:
        # Google rate-limited us — skip safely
        print("Google Trends rate limit hit. Skipping Google data temporarily.")

    except Exception as e:
        # Any other unexpected issue
        print(f"Google Trends error: {e}")

    return workflows
