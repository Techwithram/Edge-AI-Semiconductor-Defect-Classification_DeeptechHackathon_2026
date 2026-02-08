"""
Training script for Edge-AI semiconductor defect detection model.
YOLO-based lightweight detector optimized for edge deployment.
"""

import os
from ultralytics import YOLO

def main():
    # --- CONFIGURATION ---
    DATA_YAML = 'data.yaml'
    MODEL_TYPE = 'yolo11n.pt'  # YOLOv11 Nano (Smallest & Fastest)
    PROJECT_NAME = 'IESA_Semiconductor_Defect'
    RUN_NAME = 'run_v1_nano'
    IMG_SIZE = 640
    EPOCHS = 10   
    BATCH_SIZE = 16            # Reduce to 8 if you have low GPU memory

    # --- 1. LOAD MODEL ---
    print(f"Loading {MODEL_TYPE}...")
    model = YOLO(MODEL_TYPE) 

    # --- 2. TRAIN ---
    print("Starting Training...")
    # CRITICAL: We set geometric augmentations to 0.0 because 
    # we already handled safe rotation/flipping in your Python scripts.
    results = model.train(
        data=DATA_YAML,
        epochs=EPOCHS,
        imgsz=IMG_SIZE,
        batch=BATCH_SIZE,
        
        # --- SAFETY SETTINGS (Do not change) ---
        degrees=0.0,        # No random rotation
        fliplr=0.0,         # No random Left-Right flip (We did this manually)
        flipud=0.0,         # No random Up-Down flip (Protects the 'Cup' Vias)
        scale=0.0,          # No random zooming (We did this manually)
        
        # --- SMART LEARNING SETTINGS (Keep these) ---
        mosaic=1.0,         # Stitches 4 images together (Great for context)
        mixup=0.1,          # Blends images slightly (Good for noise)
        
        project=PROJECT_NAME,
        name=RUN_NAME,
        verbose=True
    )
    print("Training Complete!")

    # --- 3. VALIDATE ---
    print("Validating model performance...")
    metrics = model.val()
    print(f"Final mAP50-95: {metrics.box.map}")

    # --- 4. EXPORT FOR VLSI/EMBEDDED ---
    print("Exporting to ONNX format...")
    path = model.export(format="onnx")
    print(f"Model exported to: {path}")

if __name__ == '__main__':
    main()
