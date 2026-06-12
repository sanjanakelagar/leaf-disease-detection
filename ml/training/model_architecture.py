import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

def create_disease_detection_model(num_classes=39, input_shape=(224, 224, 3)):
    """
    Create a CNN model for leaf disease detection using MobileNetV2 transfer learning.
    
    Args:
        num_classes: Number of disease classes (38 diseases + 1 healthy)
        input_shape: Input image shape (height, width, channels)
    
    Returns:
        Compiled Keras model
    """
    
    # Load pre-trained MobileNetV2
    base_model = keras.applications.MobileNetV2(
        input_shape=input_shape,
        include_top=False,
        weights='imagenet'
    )
    
    # Freeze base model weights
    base_model.trainable = False
    
    # Create new model
    model = keras.Sequential([
        keras.Input(shape=input_shape),
        # Preprocessing
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.1),
        layers.RandomZoom(0.1),
        
        # Base model
        keras.applications.mobilenet_v2.preprocess_input,
        base_model,
        
        # Top layers
        layers.GlobalAveragePooling2D(),
        layers.Dense(512, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    # Compile model
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.001),
        loss='categorical_crossentropy',
        metrics=['accuracy', keras.metrics.TopKCategoricalAccuracy(k=3, name='top_3_accuracy')]
    )
    
    return model

def create_severity_model(input_shape=(224, 224, 3)):
    """
    Create a model for severity classification (mild/moderate/severe).
    """
    base_model = keras.applications.EfficientNetB0(
        input_shape=input_shape,
        include_top=False,
        weights='imagenet'
    )
    
    base_model.trainable = False
    
    model = keras.Sequential([
        keras.Input(shape=input_shape),
        keras.applications.efficientnet.preprocess_input,
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(3, activation='softmax')  # mild, moderate, severe
    ])
    
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model
