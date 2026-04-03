from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Workout Recommendation API"
    environment: str = "local"
    model_path: str = "models/current_model.pt"

    class Config:
        env_file = ".env"

settings = Settings()
