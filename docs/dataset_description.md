# Dataset Description

## 📌Overview

The dataset used in this project consists of **real semiconductor inspection images** collected from publicly available technical sources such as research publications, SEM micrographs, and educational fabrication materials. The dataset is designed to support **defect-level image classification** under edge-compute constraints, with a focus on clarity, realism, and class separability.

## 🧪Defect Classes

The current dataset includes the following **six primary defect classes** and each class contains around 200-220 datasets.

| Class | Description |
|------|------------|
| Bridge | Unintended electrical shorts between interconnects |
| LER | Line Edge Roughness from lithography variations |
| Open | Broken or missing interconnect paths |
| Via | Faulty inter-layer connections (missing/voided/misaligned) |
| CMP | Surface scratches from chemical mechanical polishing |
| Crack | Structural or stress-induced fractures |

## 🧼Clean and Other Classes

- **Clean**:  
  A separate set of defect-free inspection images is maintained to represent normal process conditions. These images are curated independently to prevent contamination of defect classes.

- **Other**:  
  An additional *Other* category is defined to capture **missing contacts**, and other ambiguous or uncommon defects that do not consistently fit into the primary defect classes. This class is intentionally curated separately and will be incrementally populated during     later stages of development.

## 🖼️Image Characteristics

- Inspection modality  : SEM-style micrographs
- Color format         : Grayscale (single-channel)
- Image quality        : Clear defect visibility with minimal background noise
- Resolution           : Standardized during preprocessing

## 📂Dataset Organization and Split

The dataset is organized following the **YOLO object detection format**, where images and labels are stored in separate directories. The current dataset includes:

- **Training set**
- **Validation set**

Each split contains:
- An `images/` directory with inspection images
- A `labels/` directory with corresponding YOLO-format annotations

This structure enables direct compatibility with YOLO-based training and evaluation pipelines.

## 🔄Dataset Evolution

The dataset is expected to evolve throughout the hackathon by:

- Incremental inclusion of clean and other-category samples
- Controlled data augmentation during training (without altering defect semantics)
- Class balancing strategies to improve model robustness

All additions will preserve the original dataset structure and labeling scheme.

