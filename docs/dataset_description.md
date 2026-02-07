# Dataset Description

### 📌Overview:

The dataset used in this project consists of **real semiconductor inspection images** collected from publicly available technical sources such as research publications, SEM micrographs, and educational fabrication materials. The dataset is designed to support **defect-level image classification** under edge-compute constraints, with a focus on clarity, realism, and class separability.

### 🧪Defect Classes:

The current dataset includes the following **six primary defect classes**:

| Class | Description | Image Count |
|------|------------|-------------|
| Bridge | Unintended electrical shorts between interconnects | 19 |
| LER | Line Edge Roughness from lithography variations | 18 |
| Open | Broken or missing interconnect paths | 16 |
| Via | Faulty inter-layer connections (missing/voided/misaligned) | 23 |
| CMP | Surface scratches from chemical mechanical polishing | 15 |
| Crack | Structural or stress-induced fractures | 18 |

### 🧼Clean and Other Classes:

- **Clean**:  
  A separate set of defect-free inspection images is maintained to represent normal process conditions. These images are curated independently to prevent contamination of defect classes.

- **Other**:  
  An additional *Other* category is defined to capture **missing contacts, merging contacts**, and other ambiguous or uncommon defects that do not consistently fit into the primary defect classes. This class is intentionally curated separately and will be incrementally    populated during later stages of development.

### 🖼️Image Characteristics:

- Inspection modality  : SEM-style micrographs
- Color format         : Grayscale (single-channel)
- Image quality        : Clear defect visibility with minimal background noise
- Resolution           : Standardized during preprocessing

### 📂Dataset Split:

At the current stage, the dataset is organized into:

- **Training set**
- **Validation set**

A dedicated **test set** will be created in later phases to evaluate generalization performance and to align with organizer-provided test data during Phase 2 of the hackathon.

### 🔄Dataset Evolution:

The dataset is expected to evolve throughout the hackathon by:

- Incremental inclusion of clean and other-category samples
- Controlled data augmentation during training (without altering defect semantics)
- Class balancing strategies to improve model robustness

All additions will preserve the original dataset structure and labeling scheme.


