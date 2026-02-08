# Dataset Overview

This directory describes the dataset used for the Edge-AI based semiconductor defect classification project developed as part of the IESA DeepTech Hackathon 2026. The dataset consists of real inspection images curated for defect-level classification under edge deployment constraints.

## 📂Dataset Organization (YOLO Format)

The dataset is organized using the **YOLO object detection format**, where images and labels are stored separately. Each image has a corresponding `.txt` annotation file containing bounding box coordinates and class IDs.

```text
dataset/
├── train/
│   ├── images/   # Training images
│   └── labels/   # YOLO-format label files
│
└── val/
    ├── images/   # Validation images
    └── labels/   # YOLO-format label files

```
## 🏷️Class Label Mapping

Each defect category is assigned a unique numerical class ID as required by the YOLO format. The mapping is consistent across training and validation datasets.

The defined classes include:
- Bridge
- Line Edge Roughness (LER)
- Open
- Via
- CMP Scratch
- Crack
- Clean
- Others

## 🖼️Image Characteristics

- Inspection images: SEM-style micrographs
- Color format: Mostly grayscale (single-channel)
- Defect visibility: Clear, defect-centric views
- Preprocessing: Applied during training (resize, normalization)

## 🔗Dataset Source

The dataset used in this project is derived from publicly available semiconductor defect inspection images curated and hosted on Kaggle.

👉 **Kaggle Dataset:**  
[Semiconductor Defect Detection Dataset](https://www.kaggle.com/datasets/ramkrishthatikonda/deeptech-hackathon/)

The dataset was further curated, filtered, and organized into YOLO-compatible training and validation splits to align with the objectives of this hackathon.


