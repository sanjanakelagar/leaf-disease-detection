# Leaf Disease Detection API Documentation

## Base URL

```
http://localhost:8000/api/v1
```

## Authentication

All endpoints (except `/auth/register` and `/auth/login`) require Bearer token:

```
Authorization: Bearer {access_token}
```

---

## Endpoints

### Auth Endpoints

#### Register User

```http
POST /auth/register
Content-Type: application/json

{
  "email": "farmer@example.com",
  "username": "farmer_john",
  "password": "secure_password",
  "first_name": "John",
  "last_name": "Farmer",
  "farm_location": "Karnataka",
  "farm_size": 50.0,
  "crops_cultivated": ["tomato", "potato"]
}

Response: 200
{
  "access_token": "jwt_token_here",
  "token_type": "bearer",
  "user_id": 1
}
```

#### Login

```http
POST /auth/login
Content-Type: application/x-www-form-urlencoded

email=farmer@example.com&password=secure_password

Response: 200
{
  "access_token": "jwt_token_here",
  "token_type": "bearer"
}
```

---

### Scan Endpoints

#### Predict Disease from Image

```http
POST /scans/predict
Content-Type: multipart/form-data
Authorization: Bearer {token}

Form Data:
  - image: <image_file>
  - crop_type: "tomato" (optional)
  - location: "Farm A" (optional)

Response: 200
{
  "scan_id": 1,
  "disease_detected": "Early Blight",
  "confidence": 0.95,
  "severity_level": "moderate",
  "affected_area_percentage": 25.5,
  "localization_map_url": "http://...",
  "original_image_url": "http://...",
  "processed_image_url": "http://...",
  "recommendations": [
    {
      "treatment_name": "Copper Fungicide",
      "description": "Apply copper fungicide spray",
      "frequency": "Every 7 days"
    }
  ],
  "fertilizer_recommendations": [
    {
      "name": "Nitrogen Rich Fertilizer",
      "npk_ratio": "20:10:10",
      "quantity": "500 kg/acre"
    }
  ]
}
```

#### Get Scan History

```http
GET /scans/history?page=1&limit=10
Authorization: Bearer {token}

Response: 200
{
  "scans": [
    {
      "scan_id": 1,
      "disease_detected": "Early Blight",
      "confidence": 0.95,
      "scan_date": "2024-01-10T10:30:00Z",
      "image_url": "http://..."
    }
  ],
  "total": 50,
  "page": 1,
  "limit": 10
}
```

#### Get Scan Details

```http
GET /scans/{scan_id}
Authorization: Bearer {token}

Response: 200
{
  "scan_id": 1,
  "disease_detected": "Early Blight",
  "confidence": 0.95,
  "severity_level": "moderate",
  "affected_area_percentage": 25.5,
  "scan_date": "2024-01-10T10:30:00Z",
  "crop_type": "tomato",
  "location": "Farm A",
  "image_url": "http://...",
  "localization_map_url": "http://...",
  "disease_info": {
    "name": "Early Blight",
    "symptoms": "Brown circular spots...",
    "causes": "Fungal infection...",
    "treatments": [...]
  }
}
```

---

### Disease Endpoints

#### Get All Diseases

```http
GET /diseases

Response: 200
[
  {
    "id": 1,
    "name": "Early Blight",
    "scientific_name": "Alternaria solani",
    "description": "Fungal disease affecting tomato leaves",
    "symptoms": "Brown spots with concentric rings",
    "affected_crops": ["tomato", "potato"]
  }
]
```

#### Get Disease Details

```http
GET /diseases/{disease_id}

Response: 200
{
  "id": 1,
  "name": "Early Blight",
  "scientific_name": "Alternaria solani",
  "description": "...",
  "symptoms": "...",
  "causes": "...",
  "affected_crops": ["tomato", "potato"],
  "treatments": [...],
  "fertilizers": [...],
  "prevention_tips": [...]
}
```

---

### User Profile Endpoints

#### Get User Profile

```http
GET /users/profile
Authorization: Bearer {token}

Response: 200
{
  "user_id": 1,
  "email": "farmer@example.com",
  "username": "farmer_john",
  "first_name": "John",
  "last_name": "Farmer",
  "farm_location": "Karnataka",
  "farm_size": 50.0,
  "crops_cultivated": ["tomato", "potato"],
  "phone": "+91-9876543210",
  "created_at": "2024-01-01T00:00:00Z",
  "total_scans": 25,
  "diseases_detected": ["Early Blight", "Late Blight"]
}
```

#### Update User Profile

```http
PUT /users/profile
Content-Type: application/json
Authorization: Bearer {token}

{
  "first_name": "John",
  "last_name": "Smith",
  "farm_size": 60.0,
  "crops_cultivated": ["tomato", "potato", "rice"]
}

Response: 200
{...updated user data...}
```

---

### Analytics Endpoints

#### Get Monthly Analytics

```http
GET /analytics/monthly?year=2024&month=1
Authorization: Bearer {token}

Response: 200
{
  "month": "2024-01",
  "total_scans": 15,
  "diseases_detected": ["Early Blight", "Late Blight"],
  "most_common_disease": "Early Blight",
  "health_score": 75.5,
  "disease_distribution": {
    "Early Blight": 10,
    "Late Blight": 5
  },
  "severity_distribution": {
    "mild": 5,
    "moderate": 7,
    "severe": 3
  }
}
```

#### Get Year Analytics

```http
GET /analytics/yearly?year=2024
Authorization: Bearer {token}

Response: 200
[
  {
    "month": "2024-01",
    "total_scans": 15,
    "health_score": 75.5,
    "most_common_disease": "Early Blight"
  },
  ...
]
```

---

## Error Responses

### 400 Bad Request

```json
{
  "error": "Invalid image format",
  "details": "Supported formats: jpg, png, gif"
}
```

### 401 Unauthorized

```json
{
  "error": "Invalid or missing authentication token"
}
```

### 404 Not Found

```json
{
  "error": "Scan not found",
  "scan_id": 999
}
```

### 500 Internal Server Error

```json
{
  "error": "Internal server error",
  "message": "Details of the error"
}
```

---

## Rate Limiting

- 100 requests per minute per user
- 10 prediction requests per minute per user

---

## Pagination

All list endpoints support:
- `page`: Page number (default: 1)
- `limit`: Items per page (default: 10, max: 100)

---

For interactive API documentation, visit: `http://localhost:8000/docs`
