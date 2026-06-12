# Machine Learning Pipeline

## Directory Structure

```
ml/
├── models/                      # Trained models
│   ├── disease_model.h5         # TensorFlow model
│   └── disease_model.tflite     # TensorFlow Lite (for mobile)
│
├── datasets/                    # Training datasets
│   ├── plantvillage/
│   └── raw_data/
│
├── preprocessing/               # Data preprocessing
│   └── preprocessing.py
│
├── training/                    # Training scripts
│   ├── train_model.py           # Main training script
│   ├── model_architecture.py    # CNN architecture
│   └── data_loader.py
│
├── evaluation/                  # Model evaluation
│   └── evaluate.py
│
└── inference/                   # Inference scripts
    └── predictor.py
```

## Quick Start

### 1. Download Dataset
```bash
python datasets/download_plantvillage.py
```

### 2. Train Model
```bash
python training/train_model.py
```

### 3. Convert to TFLite
```bash
python training/convert_to_tflite.py
```

### 4. Test Inference
```bash
python inference/predictor.py --image path/to/image.jpg
```

## Model Details

- **Architecture:** MobileNetV2 (transfer learning)
- **Input Size:** 224x224 RGB
- **Output:** Disease class + Confidence score
- **Classes:** 38 disease types + 1 healthy
- **Accuracy:** Target 95%+

## Dataset: PlantVillage

- 54,306 images
- 38 plant diseases
- 14 crop types
- Multiple lighting conditions
