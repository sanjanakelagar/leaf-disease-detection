# Setup Guide - 3 Day Sprint

## Prerequisites

- Flutter SDK
- Python 3.9+
- PostgreSQL 12+
- Git

## Backend Setup (Day 1-2)

### 1. Install Python Dependencies

```bash
cd backend
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Setup PostgreSQL Database

```bash
# Create database
psql -U postgres -c "CREATE DATABASE leaf_disease_db;"

# Run schema
psql -U postgres -d leaf_disease_db -f ../database/schema.sql
```

### 3. Configure Environment

```bash
# Copy example env file
cp .env.example .env

# Edit .env with your database credentials
```

### 4. Run Backend

```bash
python main.py

# API will be available at http://localhost:8000
# Docs: http://localhost:8000/docs
```

## ML Model Setup (Day 1)

### 1. Download Dataset

```bash
cd ml

# Download PlantVillage dataset from:
# https://github.com/spMohanty/PlantVillage-Dataset

# Extract to: ml/datasets/plantvillage/
```

### 2. Train Model

```bash
python training/train_model.py

# This will:
# - Load images from datasets/plantvillage/
# - Train the model
# - Save disease_model.h5
# - Convert to disease_model.tflite
```

## Flutter App Setup (Day 3)

### 1. Create Flutter Project

```bash
flutter create flutter_app
cd flutter_app
```

### 2. Add Dependencies

Edit `pubspec.yaml`:

```yaml
dependencies:
  flutter:
    sdk: flutter
  
  # HTTP & API
  http: ^1.1.0
  dio: ^5.3.0
  
  # State Management
  riverpod: ^2.4.0
  flutter_riverpod: ^2.4.0
  
  # Database
  sqflite: ^2.3.0
  path: ^1.8.3
  
  # Camera
  camera: ^0.10.5
  image_picker: ^1.0.4
  
  # Image Processing
  image: ^4.0.17
  
  # UI
  provider: ^6.0.0
  fl_chart: ^0.63.0
  shimmer: ^3.0.0
  
  # Navigation
  go_router: ^11.0.0
  
  # Utilities
  intl: ^0.18.1
  shared_preferences: ^2.2.0
```

### 3. Get Dependencies

```bash
flutter pub get
```

### 4. Run App

```bash
flutter run
```

## Quick Health Checks

### Backend Health

```bash
curl http://localhost:8000/health

# Expected response:
# {"status": "healthy", "app": "Leaf Disease Detection API"}
```

### API Docs

Visit: http://localhost:8000/docs

## Troubleshooting

### Database Connection Error

```bash
# Check PostgreSQL is running
psql -U postgres -c "\list"

# Update DATABASE_URL in .env
```

### Missing ML Model

```bash
# Run training
cd ml && python training/train_model.py
```

### Flutter Build Issues

```bash
flutter clean
flutter pub get
flutter run
```

## Environment Variables

Create `.env` file:

```
DATABASE_URL=postgresql://postgres:password@localhost:5432/leaf_disease_db
SECRET_KEY=your-secret-key
DEBUG=True
API_HOST=0.0.0.0
API_PORT=8000
```

---

**Next Step:** Follow the daily sprint schedule in README.md
