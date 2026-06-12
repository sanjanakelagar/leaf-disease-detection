# Day 1 Sprint: Foundation & ML Model Setup

## Objectives (8-10 hours)

✅ Setup project repository structure
✅ Configure Python environment
✅ Setup PostgreSQL database
✅ Download PlantVillage dataset
✅ Train CNN model
✅ Convert model to TensorFlow Lite
✅ Create backend API skeleton

## Timeline

### Hour 0-1: Environment Setup

```bash
# Clone/navigate to repository
cd leaf-disease-detection

# Create Python virtual environment
cd backend
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Hour 1-2: Database Setup

```bash
# Start PostgreSQL
# On macOS: brew services start postgresql
# On Linux: sudo systemctl start postgresql
# On Windows: Start from Services

# Create database
psql -U postgres -c "CREATE DATABASE leaf_disease_db;"

# Run schema
psql -U postgres -d leaf_disease_db -f ../database/schema.sql

# Create admin user
psql -U postgres -d leaf_disease_db -c "
INSERT INTO users (email, username, password_hash, first_name, last_name)
VALUES ('admin@example.com', 'admin', 'hashed_password', 'Admin', 'User');
"
```

### Hour 2-3: Backend Setup

```bash
# Configure environment
cp .env.example .env

# Edit .env with your database URL:
# DATABASE_URL=postgresql://postgres:password@localhost:5432/leaf_disease_db

# Test backend
python main.py

# Visit: http://localhost:8000/health
# Should return: {"status": "healthy", ...}
```

### Hour 3-5: ML Model - Dataset Preparation

```bash
cd ../ml

# Download PlantVillage dataset
# Option 1: From GitHub
git clone https://github.com/spMohanty/PlantVillage-Dataset.git
cp PlantVillage-Dataset/raw/color ~/leaf-disease-detection/ml/datasets/plantvillage

# Option 2: From Zenodo (faster)
wget https://zenodo.org/records/5716578/files/plantvillage-dataset-color.zip
unzip plantvillage-dataset-color.zip -d datasets/
```

### Hour 5-8: Train Model

```bash
# Navigate to ML directory
cd ../ml

# Run training
python training/train_model.py

# This will:
# 1. Load all images (54K+ images)
# 2. Split into train/val/test (70/15/15)
# 3. Train MobileNetV2 model (≈3-4 hours)
# 4. Save disease_model.h5
# 5. Convert to disease_model.tflite
```

### Hour 8-10: Backend API Enhancement

```bash
cd ../backend

# Create prediction route
# File: app/api/predictions.py
```

## Deliverables at End of Day 1

✅ **Repository Structure Created**
   - folders/files organized
   - .gitignore configured

✅ **Backend Running**
   - FastAPI server on http://localhost:8000
   - Health check endpoint working
   - Database connected

✅ **ML Model Trained**
   - disease_model.h5 (≈150MB)
   - disease_model.tflite (≈50MB)
   - class_names.json with 39 classes
   - Expected Accuracy: 90%+

✅ **API Skeleton**
   - /health endpoint
   - /auth endpoints structure
   - /scans endpoints structure

## Key Files Created

- `backend/main.py` - FastAPI app
- `backend/config.py` - Configuration
- `backend/requirements.txt` - Dependencies
- `ml/training/train_model.py` - Training script
- `ml/training/model_architecture.py` - CNN architecture
- `database/schema.sql` - Database schema
- `flutter_app/pubspec.yaml` - Flutter dependencies

## Troubleshooting

### Dataset Download Issues

If download is slow:
```bash
# Alternative: Use smaller subset
cd ml/datasets/plantvillage
ls -d */ | head -5  # Take first 5 diseases
```

### Model Training Too Slow

```bash
# In train_model.py, reduce:
epochs=10  # Instead of 20
batch_size=64  # Instead of 32
```

### Database Connection Error

```bash
# Check PostgreSQL
psql -U postgres -c "\list"

# Update .env with correct credentials
```

## Next Steps

→ **Day 2:** Build complete Backend API with all endpoints
→ **Day 3:** Build Flutter mobile app with UI and integration

---

**Status:** Ready for Day 2 after successful completion
