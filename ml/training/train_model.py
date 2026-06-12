import os
import json
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from sklearn.model_selection import train_test_split
from model_architecture import create_disease_detection_model

class DiseaseModelTrainer:
    def __init__(self, dataset_path='../datasets/plantvillage', model_save_path='../models'):
        self.dataset_path = dataset_path
        self.model_save_path = model_save_path
        self.class_names = []
        self.disease_info = {}
        os.makedirs(model_save_path, exist_ok=True)
    
    def load_dataset(self):
        """
        Load images from dataset directory structure.
        Assumes structure: dataset/disease_name/image.jpg
        """
        print("Loading dataset...")
        images = []
        labels = []
        
        if not os.path.exists(self.dataset_path):
            print(f"Dataset not found at {self.dataset_path}")
            print("Downloading PlantVillage dataset...")
            self._download_dataset()
        
        # Get all disease directories
        disease_dirs = sorted([d for d in os.listdir(self.dataset_path) 
                              if os.path.isdir(os.path.join(self.dataset_path, d))])
        self.class_names = disease_dirs
        
        print(f"Found {len(self.class_names)} disease classes")
        print(f"Classes: {self.class_names}")
        
        # Load images
        for idx, disease in enumerate(self.class_names):
            disease_path = os.path.join(self.dataset_path, disease)
            image_files = [f for f in os.listdir(disease_path) 
                          if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
            
            for img_file in image_files:
                img_path = os.path.join(disease_path, img_file)
                try:
                    img = image.load_img(img_path, target_size=(224, 224))
                    img_array = image.img_to_array(img)
                    images.append(img_array)
                    labels.append(idx)
                except Exception as e:
                    print(f"Error loading {img_path}: {e}")
        
        return np.array(images), np.array(labels)
    
    def _download_dataset(self):
        """Download PlantVillage dataset (placeholder)"""
        print("""
        To download PlantVillage dataset:
        1. Visit: https://github.com/spMohanty/PlantVillage-Dataset
        2. Download the dataset
        3. Extract to ml/datasets/plantvillage/
        
        OR use: 
        wget https://zenodo.org/records/5716578/files/plantvillage-dataset-color.zip
        unzip and extract to ml/datasets/plantvillage/
        """)
    
    def train(self, epochs=20, batch_size=32, validation_split=0.2):
        """
        Train the disease detection model.
        """
        # Load data
        X, y = self.load_dataset()
        
        if len(X) == 0:
            print("No images found. Please download dataset first.")
            return None
        
        print(f"Dataset size: {len(X)} images")
        
        # Normalize images
        X = X.astype('float32') / 255.0
        
        # Convert labels to one-hot
        y = keras.utils.to_categorical(y, num_classes=len(self.class_names))
        
        # Split data
        X_train, X_temp, y_train, y_temp = train_test_split(
            X, y, test_size=0.3, random_state=42
        )
        X_val, X_test, y_val, y_test = train_test_split(
            X_temp, y_temp, test_size=0.5, random_state=42
        )
        
        print(f"Training set: {len(X_train)}")
        print(f"Validation set: {len(X_val)}")
        print(f"Test set: {len(X_test)}")
        
        # Create model
        model = create_disease_detection_model(num_classes=len(self.class_names))
        print(model.summary())
        
        # Callbacks
        callbacks = [
            keras.callbacks.EarlyStopping(
                monitor='val_loss',
                patience=5,
                restore_best_weights=True
            ),
            keras.callbacks.ReduceLROnPlateau(
                monitor='val_loss',
                factor=0.5,
                patience=3,
                min_lr=1e-7
            )
        ]
        
        # Train model
        print("\nTraining model...")
        history = model.fit(
            X_train, y_train,
            validation_data=(X_val, y_val),
            epochs=epochs,
            batch_size=batch_size,
            callbacks=callbacks,
            verbose=1
        )
        
        # Evaluate
        print("\nEvaluating model...")
        test_loss, test_acc, test_top3 = model.evaluate(X_test, y_test, verbose=0)
        print(f"Test Accuracy: {test_acc:.4f}")
        print(f"Test Top-3 Accuracy: {test_top3:.4f}")
        
        # Save model
        model_path = os.path.join(self.model_save_path, 'disease_model.h5')
        model.save(model_path)
        print(f"\nModel saved to {model_path}")
        
        # Save class names
        classes_path = os.path.join(self.model_save_path, 'class_names.json')
        with open(classes_path, 'w') as f:
            json.dump(self.class_names, f)
        
        # Convert to TFLite
        self._convert_to_tflite(model)
        
        return model, history
    
    def _convert_to_tflite(self, model):
        """
        Convert TensorFlow model to TFLite for mobile deployment.
        """
        print("\nConverting to TensorFlow Lite...")
        converter = tf.lite.TFLiteConverter.from_keras_model(model)
        converter.optimizations = [tf.lite.Optimize.DEFAULT]
        tflite_model = converter.convert()
        
        tflite_path = os.path.join(self.model_save_path, 'disease_model.tflite')
        with open(tflite_path, 'wb') as f:
            f.write(tflite_model)
        
        print(f"TFLite model saved to {tflite_path}")

if __name__ == "__main__":
    trainer = DiseaseModelTrainer()
    model, history = trainer.train(epochs=20, batch_size=32)
