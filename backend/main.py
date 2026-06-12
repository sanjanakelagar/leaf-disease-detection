from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
import os

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create upload directory
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

# Health Check
@app.get("/health")
async def health_check():
    return {"status": "healthy", "app": settings.APP_NAME}

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Leaf Disease Detection API", "version": settings.APP_VERSION}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
