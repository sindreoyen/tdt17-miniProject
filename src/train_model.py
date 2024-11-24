print("Importing ultralytics...")
import os
from ultralytics import YOLO

print("Training model...")
# Path to model with pre-trained weights
__pretrained_model = os.path.join("..", "models", "pre-trained", "yolo11s.pt") # COCO pre-trained model
__data = os.path.join("train", "data.yaml") # Data file

# Train the model
pretrained = YOLO(__pretrained_model)
result = pretrained.train(data=__data, 
                          epochs=20, 
                          imgsz=1024, 
                          device=[0, 1])