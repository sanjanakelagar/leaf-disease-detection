# Leaf Disease Detection Mobile App

An AI-powered Flutter mobile application for real-time plant leaf disease detection, localization, and treatment recommendations.

## 📱 Project Overview

This app combines Computer Vision (CNN) and Machine Learning to:
- ✅ Capture/upload plant leaf images
- ✅ Detect diseases in real-time using CNN
- ✅ Localize affected areas with visual overlay
- ✅ Provide detailed disease information
- ✅ Store scan history and user profile
- ✅ Generate monthly analytics graphs
- ✅ Recommend fertilizers and treatments

## 🏗️ Architecture

```
Flutter Mobile App (Dart)
       ↓
Python FastAPI Backend
       ↓
TensorFlow CNN Model
       ↓
PostgreSQL Database
```

## 📂 Project Structure

```
leaf-disease-detection/
├── flutter_app/              # Flutter Mobile App
│   ├── lib/
│   │   ├── screens/
│   │   ├── widgets/
│   │   ├── models/
│   │   ├── services/
│   │   ├── providers/
│   │   └── main.dart
│   └── pubspec.yaml
│
├── backend/                  # Python FastAPI Server
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   ├── requirements.txt
│   └── config.py
│
├── ml/                       # Machine Learning
│   ├── models/               # Trained models
│   ├── training/
│   ├── preprocessing/
│   └── datasets/
│
├── database/                 # Database Schemas
│   └── schema.sql
│
├── docs/                     # Documentation
│   ├── API.md
│   ├── SETUP.md
│   └── ARCHITECTURE.md
│
└── .gitignore
```

## 🚀 3-Day Sprint Timeline

| Day | Focus | Deliverable |
|-----|-------|-------------|
| **Day 1** | ML Model Setup | Trained CNN + Model conversion + API skeleton |
| **Day 2** | Backend & DB | Full FastAPI + PostgreSQL + Image processing |
| **Day 3** | Flutter App | Complete UI + Camera + History + Analytics |

## 🛠️ Tech Stack

**Frontend:** Flutter (Dart)
**Backend:** FastAPI (Python)
**ML:** TensorFlow/PyTorch, OpenCV
**Database:** PostgreSQL
**Storage:** Firebase Cloud Storage (optional)

---

**Status:** 🔄 Active Development (3-Day Sprint)
**Created:** 2026-06-12
