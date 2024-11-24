print("Importing ultralytics...")
import os
from ultralytics import YOLO

print("Training model...")
# Path to model with pre-trained weights
__pretrained_model = os.path.join("models", "pre-trained", "yolo11s.pt") # COCO pre-trained model

# Train the model
pretrained = YOLO(__pretrained_model)
result = pretrained.train(
    data="data.yaml", 
    epochs=100, 
    imgsz=1024, 
    device=[0, 1], 
    show_labels=False, 
    patience=10, 
    # Augmentation
    degrees=2.0,          # Slight rotation
    scale=0.4,            # Slight scaling
    translate=0.1,        # Translation in image plane
    shear=2.0,            # Slight shearing
    mosaic=1.0,           # Mosaic augmentation
    hsv_h=0.015,          # Slight hue adjustment
    hsv_s=0.5,            # Moderate saturation adjustment
    hsv_v=0.4,            # Brightness adjustment
    label_smoothing=0.05, # Slight label smoothing
)
