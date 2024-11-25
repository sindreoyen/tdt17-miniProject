print("Importing ultralytics...")
import os
from ultralytics import YOLO

print("Training model...")
# Path to model with pre-trained weights
__pretrained_model = os.path.join("models", "pre-trained", "yolo11s.pt") # COCO pre-trained model

# Train the model
pretrained = YOLO(model=__pretrained_model)
result = pretrained.train(
    data="data.yaml", # Path to data.yaml
    pretrained=True, # Use pre-trained model
    batch=16, # Batch size
    epochs=100, # Number of epochs
    imgsz=1024, # Image size
    device=[0, 1], # Train on GPU 0 and 1
    patience=10, # Early stopping patience
    workers=4, # Number of workers
    lr0=0.01, # Initial learning rate
    # Augmentation
    degrees=2.0,          # Slight rotation
    scale=0.4,            # Slight scaling
    translate=0.1,        # Translation in image plane
    shear=2.0,            # Slight shearing
    hsv_h=0.015,          # Slight hue adjustment
    hsv_s=0.5,            # Moderate saturation adjustment
    hsv_v=0.4,            # Brightness adjustment
    mosaic=1.0,           # Mosaic augmentation
    label_smoothing=0.05, # Slight label smoothing
)
