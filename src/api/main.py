import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from src.api.routes import router

app = FastAPI(
    title="Personalized Workout Recommendation API",
    description="MLOps backend to recommend workout programs based on user inputs.",
    version="1.0.0"
)

# Include the endpoints router
app.include_router(router, prefix="/api/v1")

# Mount static files for the UI
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
async def serve_ui():
    return FileResponse(os.path.join(static_dir, "index.html"))

if __name__ == "__main__":
    import uvicorn
    # uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=8000, reload=True)
