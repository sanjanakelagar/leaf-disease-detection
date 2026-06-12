# Day 2 Sprint: Backend API & Database Integration

## Objectives (8-10 hours)

✅ Complete all backend API endpoints
✅ Implement ML inference pipeline
✅ Setup image processing (Grad-CAM visualization)
✅ Implement authentication (JWT)
✅ Populate disease database
✅ Create API documentation
✅ Test all endpoints

## Timeline

### Hour 0-1: ML Inference Integration

```bash
cd backend

# Create prediction service
# File: app/services/ml_service.py
```

**Key Functions:**
- Load TFLite model
- Preprocess image
- Run inference
- Generate confidence scores
- Apply Grad-CAM for visualization

### Hour 1-3: Image Processing

**File:** `app/services/image_processor.py`

```python
# Key functions:
- load_and_preprocess_image()
- apply_gradcam()
- create_overlay_image()
- save_processed_image()
```

### Hour 3-5: API Routes Development

**Files to create:**

1. `app/api/auth.py` - Authentication endpoints
   - POST /auth/register
   - POST /auth/login
   - POST /auth/logout

2. `app/api/scans.py` - Scan endpoints
   - POST /scans/predict
   - GET /scans/history
   - GET /scans/{scan_id}
   - POST /scans/{scan_id}/feedback

3. `app/api/diseases.py` - Disease endpoints
   - GET /diseases
   - GET /diseases/{disease_id}
   - POST /diseases (admin)

4. `app/api/users.py` - User endpoints
   - GET /users/profile
   - PUT /users/profile
   - DELETE /users/profile

5. `app/api/analytics.py` - Analytics endpoints
   - GET /analytics/monthly
   - GET /analytics/yearly

### Hour 5-7: Database Models & Schemas

**Files to create:**

1. `app/models/database.py` - SQLAlchemy models
2. `app/schemas/user.py` - Pydantic schemas
3. `app/schemas/scan.py` - Scan schemas
4. `app/schemas/disease.py` - Disease schemas

### Hour 7-8: Populate Disease Database

```bash
# Create seed script
# File: database/seed_diseases.py

# This will insert:
# - 38 plant diseases
# - Symptoms, treatments, fertilizers
# - Recommendations
```

### Hour 8-10: Testing & Documentation

```bash
# Visit http://localhost:8000/docs
# Test all endpoints interactively
# Create unit tests
```

## Files to Create This Day

### 1. Service Layer

```
app/services/
├── ml_service.py          # Model inference
├── image_processor.py     # Image processing
├── auth_service.py        # JWT tokens
├── user_service.py        # User logic
├── scan_service.py        # Scan logic
└── analytics_service.py   # Analytics
```

### 2. API Routes

```
app/api/
├── auth.py                # Auth endpoints
├── scans.py               # Scan endpoints
├── diseases.py            # Disease endpoints
├── users.py               # User endpoints
├── analytics.py           # Analytics endpoints
└── __init__.py
```

### 3. Data Models

```
app/models/
├── database.py            # SQLAlchemy models
└── __init__.py

app/schemas/
├── user.py                # User schemas
├── scan.py                # Scan schemas
├── disease.py             # Disease schemas
└── __init__.py
```

## Key Implementations

### 1. ML Inference

```python
# Pseudo code
def predict_disease(image_path):
    # Load model
    model = load_tflite_model()
    
    # Preprocess
    image = preprocess_image(image_path)
    
    # Predict
    predictions = model.predict(image)
    
    # Get top predictions
    top_3 = get_top_3_predictions(predictions)
    
    # Grad-CAM visualization
    heat_map = generate_gradcam(image, model)
    overlay = create_overlay(image, heat_map)
    
    return {
        'disease': top_3[0]['class'],
        'confidence': top_3[0]['score'],
        'alternatives': top_3[1:],
        'visualization': overlay
    }
```

### 2. Image Processing (Grad-CAM)

```python
def generate_gradcam(image, model, class_index):
    # Compute gradients
    # Create attention map
    # Apply colormap
    # Return visualization
    pass
```

### 3. Authentication

```python
def create_access_token(data: dict):
    # Create JWT token
    # Return token with expiration
    pass

async def get_current_user(token: str):
    # Verify token
    # Return user object
    pass
```

## Deliverables at End of Day 2

✅ **Full Backend API**
   - All endpoints implemented
   - Authentication working
   - Database integration complete

✅ **ML Integration**
   - Inference working
   - Image processing complete
   - Grad-CAM visualization

✅ **Database Populated**
   - 38 diseases with info
   - Treatments and recommendations
   - Fertilizer data

✅ **API Documentation**
   - Interactive Swagger UI at /docs
   - API.md file updated
   - All endpoints tested

## Testing Checklist

- [ ] POST /auth/register - Create user
- [ ] POST /auth/login - Login user
- [ ] POST /scans/predict - Upload image and get prediction
- [ ] GET /scans/history - Get user's scan history
- [ ] GET /diseases - Get all diseases
- [ ] GET /users/profile - Get user profile
- [ ] GET /analytics/monthly - Get analytics

## API Response Example

```json
POST /scans/predict
{
  "scan_id": 1,
  "disease_detected": "Early Blight",
  "confidence": 0.952,
  "severity_level": "moderate",
  "affected_area_percentage": 25.5,
  "image_url": "http://localhost:8000/uploads/scan_1.jpg",
  "visualization_url": "http://localhost:8000/uploads/scan_1_viz.jpg",
  "disease_info": {
    "name": "Early Blight",
    "symptoms": "Brown spots with concentric rings",
    "treatments": [...],
    "fertilizers": [...]
  }
}
```

## Next Steps

→ **Day 3:** Build Flutter mobile app and integrate with backend

---

**Status:** Backend API complete and ready for mobile integration
