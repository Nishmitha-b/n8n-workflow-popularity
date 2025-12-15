---

# n8n Workflow Popularity System

## Overview

A production-ready system that identifies the **most popular n8n workflows** across multiple platforms using **real, verifiable popularity signals**.
Results are exposed via a **REST API** and updated automatically using **cron jobs**.

---

## Data Sources & Metrics

### YouTube (n8n workflow videos)

* Views, Likes, Comments
* Engagement ratios:

  * `like_to_view_ratio`
  * `comment_to_view_ratio`

### n8n Community Forum (Discourse)

* Thread views
* Likes
* Replies
* Contributors
* Engagement ratios

### Google Search (Trends)

* Average search interest (last 3 months)
* Country-specific demand (US / IN)

> Google Trends rate limits are handled gracefully without API failure.

---

## API
## Environment Variables

This project uses external APIs.

Create a `.env` file in the root directory:

YOUTUBE_API_KEY=your_api_key_here

The `.env` file is excluded from version control for security reasons.

### Endpoint

```
GET /api/workflows
```

### Query Parameters

* `platform` → YouTube | Forum | Google
* `country` → US | IN

### Sample Response

```
{
  "workflow": "Google Sheets → Slack Automation",
  "platform": "YouTube",
  "popularity_metrics": {
    "views": 12500,
    "likes": 630,
    "comments": 88,
    "like_to_view_ratio": 0.05,
    "comment_to_view_ratio": 0.007
  },
  "country": "US"
}
```

---

## Automation

A cron-ready job (`cron/fetch_data.py`) fetches and refreshes popularity data on a daily or weekly schedule.

---

## Scalability

The system is designed to scale to **tens of thousands of workflows** through:

* API pagination
* Keyword expansion
* Scheduled cron execution

The current dataset demonstrates functionality with a representative sample.

---

## How to Run

```
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Deliverables

* ✅ Working REST API
* ✅ 50+ workflows with real popularity evidence
* ✅ Country segmentation (US / IN / Global)
* ✅ Cron-ready automation
* ✅ Production-ready code

---

## Final Note

This project focuses on **real data, clean architecture, and production readiness**, aligning closely with real-world backend systems.

---

