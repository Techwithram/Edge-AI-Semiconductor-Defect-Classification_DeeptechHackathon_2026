# Dataset Overview

This directory describes the dataset used for the Edge-AI based semiconductor defect classification project developed as part of the IESA DeepTech Hackathon 2026. The dataset consists of real inspection images curated for defect-level classification under edge deployment constraints.

## 📂Dataset Organization

The dataset is organized using a folder-based labeling scheme compatible with standard deep learning frameworks:

```
dataset/
├── train/
│   ├── bridge/
│   ├── ler/
│   ├── open/
│   ├── via/
│   ├── cmp/
│   ├── crack/
│   └── clean/
│
└── val/
    ├── bridge/
    ├── ler/
    ├── open/
    ├── via/
    ├── cmp/
    ├── crack/
    └── clean/
```
## 🖼️Image Characteristics

- Inspection images: SEM-style micrographs
- Color format: Mostly grayscale (single-channel)
- Defect visibility: Clear, defect-centric views
- Preprocessing: Applied during training (resize, normalization)

## ⚠️Dataset Availability

Due to size constraints and source licensing considerations, the full dataset images are not uploaded to this repository. This repository provides the dataset structure, documentation, and processing pipeline to ensure reproducibility and transparency.



