from fastapi import APIRouter, HTTPException
from src.api.schemas import RecommendationRequest, RecommendationResponse, WorkoutExercise

router = APIRouter()

@router.post("/recommend", response_model=RecommendationResponse)
async def get_recommendation(request: RecommendationRequest):
    # This is a placeholder logic for the ML model
    # Eventually, we will pass request data to our PyTorch model inference script here!
    
    # Dummy recommendation based on logic setup
    exercises = [
        WorkoutExercise(name="Squat", sets=4, reps="10-12", rest_seconds=90),
        WorkoutExercise(name="Deadlift", sets=3, reps="8", rest_seconds=120)
    ]
    
    return RecommendationResponse(
        program_name="Beginner Strength & Hypertrophy",
        difficulty_level="Beginner",
        exercises=exercises,
        estimated_duration_minutes=45
    )

@router.get("/health")
async def health_check():
    return {"status": "healthy", "service": "workout-recommendation-api"}
