from fastapi import APIRouter, HTTPException
from src.api.schemas import RecommendationRequest, RecommendationResponse, WorkoutExercise

router = APIRouter()

@router.post("/recommend", response_model=RecommendationResponse)
async def get_recommendation(request: RecommendationRequest):
    # This is a placeholder logic for the ML model
    # Eventually, we will pass request data to our PyTorch model inference script here!
    
    goal = request.goals.primary_goal
    if goal == "strength":
        exercises = [
            WorkoutExercise(name="Barbell Back Squat", sets=5, reps="3-5", rest_seconds=180),
            WorkoutExercise(name="Deadlift", sets=3, reps="3-5", rest_seconds=240)
        ]
        prog_name = "Power & Strength Focus"
    elif goal == "diet":
        exercises = [
            WorkoutExercise(name="Jump Squat", sets=4, reps="15-20", rest_seconds=45),
            WorkoutExercise(name="Kettlebell Swings", sets=4, reps="20", rest_seconds=45)
        ]
        prog_name = "High Intensity Fat Loss"
    else: # bodybuilding
        exercises = [
            WorkoutExercise(name="Leg Press", sets=4, reps="10-12", rest_seconds=90),
            WorkoutExercise(name="Dumbbell Lunges", sets=3, reps="12-15", rest_seconds=90)
        ]
        prog_name = "Hypertrophy Aesthetics"
    
    return RecommendationResponse(
        program_name=prog_name,
        difficulty_level="Intermediate",
        exercises=exercises,
        estimated_duration_minutes=60
    )

@router.get("/health")
async def health_check():
    return {"status": "healthy", "service": "workout-recommendation-api"}
