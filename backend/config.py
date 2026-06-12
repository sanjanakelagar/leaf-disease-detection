import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # App
    APP_NAME = "Leaf Disease Detection API"
    APP_VERSION = "1.0.0"
    DEBUG = os.getenv("DEBUG", "True") == "True"
    
    # Database
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://user:password@localhost:5432/leaf_disease_db"
    )
    
    # JWT
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    # File Upload
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "gif"}
    UPLOAD_DIR = "./uploads"
    
    # ML Model
    MODEL_PATH = "../ml/models/disease_model.h5"
    MODEL_TFLITE_PATH = "../ml/models/disease_model.tflite"
    
    # API
    API_V1_STR = "/api/v1"
    
    # CORS
    ALLOWED_ORIGINS = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ]

settings = Settings()
