from fastapi import FastAPI
from app.api.workflows import router as workflow_router

app = FastAPI(title="n8n Workflow Popularity API")

app.include_router(workflow_router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "API is running"}
