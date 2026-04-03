from pydantic import BaseModel, Field
from typing import List, Optional

class UserDemographics(BaseModel):
    age: int = Field(..., gt=0, description="User's age in years")
    gender: str = Field(..., description="User's gender (e.g., 'male', 'female', 'other')")

class FitnessGoals(BaseModel):
    current_weight_kg: float = Field(..., gt=0, description="User's current weight in kg")
    target_weight_kg: float = Field(..., gt=0, description="User's target weight in kg")
    target_muscle_mass_kg: Optional[float] = Field(None, description="User's target muscle mass in kg (optional)")

class RecommendationRequest(BaseModel):
    user_info: UserDemographics
    goals: FitnessGoals

class WorkoutExercise(BaseModel):
    name: str = Field(..., description="Name of the exercise")
    sets: int = Field(..., description="Recommended number of sets")
    reps: str = Field(..., description="Recommended repetitions per set")
    rest_seconds: int = Field(..., description="Rest time between sets in seconds")

class RecommendationResponse(BaseModel):
    program_name: str
    difficulty_level: str
    exercises: List[WorkoutExercise]
    estimated_duration_minutes: int
