# Edge-AI-Semiconductor-Defect-Classification_DeeptechHackathon_2026
This repository presents an edge-AI based defect classification system for wafer/die inspection happening in semiconductor fabrication industries.

[![Hackathon](https://img.shields.io/badge/DeepTech_Hackathon%202026-blue)](https://i4c.in/iesa-hackathon/#ps-iesa)
[![Edge AI](https://img.shields.io/badge/Edge_AI-green)](#)
[![Semiconductor](https://img.shields.io/badge/Semiconductor_Inspection-purple)](#)
[![IESA](https://img.shields.io/badge/Organized%20by-IESA-orange)](https://www.iesaonline.org)
[![NXP](https://img.shields.io/badge/Sponsored%20by-NXP-red)](https://www.nxp.com)
[![GF](https://img.shields.io/badge/Sponsored%20by-GlobalFoundries-darkblue)](https://www.globalfoundries.com)
[![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)](#)

### Introduction:

Semiconductor manufacturing involves hundreds of tightly controlled fabrication steps, where even microscopic defects can lead to yield loss or catastrophic device failure. Modern fabs generate massive volumes of inspection images using tools such as optical microscopes, SEM, and defect review systems. Traditional centralized inspection pipelines suffer from high latency, heavy bandwidth usage, and poor scalability. This project explores an **Edge-AI based defect classification system** that enables fast, on-device inference aligned with Industry 4.0 manufacturing requirements.

### 🎯Hackathon Objective:

The objective of this project is to design and demonstrate an **Edge-AI capable
defect classification system** that can:

- Detect and classify semiconductor wafer/die defects into predefined categories
- Achieve strong accuracy using lightweight, edge-friendly models
- Enable real-time, high-volume inspection workflows
- Be portable to NXP eIQ deployment flows targeting i.MX RT series devices

### 🧪Defect Classes Considered:

The defect classes were selected to represent **commonly observed and manufacturing-critical failure modes** across semiconductor fabrication processes such as lithography, etching, CMP, and interconnect formation. The classification scheme balances **realism, separability, and edge feasibility**.

[![Bridge](https://img.shields.io/badge/Bridge_Defects-red)](#)
[![LER](https://img.shields.io/badge/LER-blue)](#)
[![Open](https://img.shields.io/badge/Open_Defects-orange)](#)
[![Via](https://img.shields.io/badge/Malformed_Vias-purple)](#)
[![CMP](https://img.shields.io/badge/CMP_Scratches-green)](#)
[![Crack](https://img.shields.io/badge/Crack_Defects-darkred)](#)
[![Clean](https://img.shields.io/badge/Clean[Defect_free]-brightgreen)](#)
[![Other](https://img.shields.io/badge/Other[Miscellaneous]-grey)](#)


### 🔹 Primary Defect Classes:

- **Bridge Defects**  
  Unintended electrical connections formed between adjacent metal lines, typically caused by lithography or etching errors.

- **Line Edge Roughness (LER)**  
  Irregular or rough edges along patterned lines, primarily introduced during lithography, impacting device variability and reliability.

- **Open Defects**  
  Discontinuities or breaks in interconnect lines resulting in missing electrical paths.

- **Via Defects**  
  Missing, voided, misaligned, or partially filled vias that disrupt vertical inter-layer connectivity.

- **CMP Scratches**  
  Surface-level scratches and damage introduced during chemical mechanical polishing, potentially affecting downstream layers.

- **Crack Defects**  
  Structural cracks caused by mechanical stress, thermal cycling, or process non-uniformities.

### 🔹 Auxiliary Classes:

- **Clean**  
  Defect-free semiconductor structures exhibiting uniform geometry and process-consistent patterns. This class is critical to prevent false positives during inspection.

- **Other**  
  A catch-all category that includes **missing contacts, merging contacts**, and other uncommon or ambiguous defects that do not consistently belong to the primary classes.

### 📋Class Summary:

| Category Type | Defect Class | Description |
|--------------|-------------|-------------|
| Primary | Bridge | Unintended interconnect shorts |
| Primary | LER | Rough line edges from lithography |
| Primary | Open | Broken or missing connections |
| Primary | Via | Faulty inter-layer connections |
| Primary | CMP | Polishing-induced surface scratches |
| Primary | Crack | Structural or stress-induced fractures |
| Auxiliary | Clean | Defect-free structures |
| Auxiliary | Other | Missing contacts, merging contacts, misc. |

### 🧠Design Philosophy:

This project follows a **practical Edge-AI philosophy**, i.e., accuracy alone is not sufficient; models must be efficient, portable, and compatible with real-world edge deployment constraints.

Key principles include:
- Dataset quality over model complexity
- Lightweight architectures over deep, resource-heavy networks
- Clear separation between data preparation, training, and deployment
- Early consideration of model portability and conversion formats

### 🔄Edge-AI Development Pipeline:

| Stage | Description | Key Output |
|------|------------|-----------|
| D0 | Dataset collection & curation | Labeled inspection images |
| D1 | Preprocessing & normalization | ML-ready input tensors |
| D2 | Model training & validation | Trained lightweight CNN |
| D3 | Model evaluation | Accuracy, Precision, Recall |
| D4 | Model export | ONNX model |
| D5 | Edge porting | NXP eIQ-compatible artifacts |

### 📁Repository Structure:
```
Edge-AI-Semiconductor-Defect-Classification_DeeptechHackathon_2026/
├── dataset/        # Dataset structure & description
├── src/            # Preprocessing, training, inference code
├── models/         # Trained models (ONNX)
├── results/        # Evaluation metrics & confusion matrices
├── docs/           # Detailed documentation
└── README.md








  


