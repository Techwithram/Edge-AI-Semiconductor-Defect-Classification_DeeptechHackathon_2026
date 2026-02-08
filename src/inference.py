"""
Inference script for semiconductor defect detection
"""

import os
from ultralytics import YOLO

# --- CONFIGURATION ---
MODEL_PATH = "models/unquantized/model.onnx"
INPUT_SOURCE = "results/samples"
OUTPUT_DIR = "results/inference_outputs"
CONF_THRESHOLD = 0.25


def run_inference():
    if not os.path.exists(MODEL_PATH):
        print(f"❌ Model not found at {MODEL_PATH}")
        return

    print(f"Loading model from {MODEL_PATH}")
    model = YOLO(MODEL_PATH)

    print(f"Running inference on {INPUT_SOURCE}")
    model.predict(
        source=INPUT_SOURCE,
        conf=CONF_THRESHOLD,
        project=OUTPUT_DIR,
        name="run_1",
        save=True,
        exist_ok=True
    )

    print("✅ Inference complete. Check results/inference_outputs/")


if __name__ == "__main__":
    run_inference()
