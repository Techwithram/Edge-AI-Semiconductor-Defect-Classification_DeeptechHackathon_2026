# Project Approach

## 📌Problem Understanding

Semiconductor fabrication processes generate large volumes of inspection images at various stages such as lithography, etching, CMP, and interconnect formation. Microscopic defects introduced at any stage can significantly impact yield and device reliability. Traditional inspection pipelines rely on centralized analysis or manual review, which introduces latency, bandwidth bottlenecks, and scalability limitations. For modern high-throughput fabs, these approaches are increasingly impractical.

## ⚙️Why Edge-AI?

Edge-AI enables inference to be performed **close to the inspection tool**, rather than relying on cloud or centralized servers. This approach offers:

- Reduced latency for faster defect flagging
- Lower bandwidth usage by avoiding raw image transfer
- Improved scalability for high-volume inspection
- Better alignment with Industry 4.0 manufacturing systems

Given these advantages, this project focuses on designing an AI pipeline that is not only accurate, but also **edge-deployable and resource-efficient**.

## 🧠Problem Formulation

The defect analysis task is formulated as a **defect detection and classification** problem using a lightweight object detection approach. Instead of classifying an entire image globally, the model detects localized defect regions and assigns each detected instance to one of the predefined defect categories. The dataset is structured using the YOLO detection format, enabling efficient training of lightweight object detection models for defect localization and classification.

This formulation enables:
- Spatial localization of defects
- Improved interpretability of predictions
- Better alignment with practical semiconductor inspection workflows

The approach is designed to balance detection performance with edge deployment constraints.

## 🧪Dataset-Centric Approach

The project follows a **dataset-first methodology**, where emphasis is placed on data quality, class clarity, and realistic defect representation rather than on overly complex models.

Key considerations include:
- Use of real inspection images collected from public technical sources
- Clear separation between defect classes to reduce label ambiguity
- Inclusion of a clean class to minimize false positives
- Planned use of an "other" class to handle uncommon or ambiguous defects

## 🧩Model Design Philosophy

The model design prioritizes **lightweight architectures** suitable for resource-constrained edge devices. Instead of deep or highly parameterized networks, the focus is on:

- Compact convolutional neural networks
- Efficient feature extraction
- Reduced memory footprint
- Faster inference times

Accuracy is balanced against model size and portability to ensure practical deployment feasibility.

## 🏋️Training Strategy

Model training is performed using Python-based machine learning frameworks. The dataset is divided into training and validation sets to monitor learning behavior and prevent overfitting. Given the limited availability of real defect images, controlled data augmentation techniques are planned during training to improve generalization without altering the underlying defect characteristics.

## 📊Evaluation Metrics

Model performance is evaluated using standard classification metrics:

- Accuracy
- Precision
- Recall
- Confusion Matrix

These metrics provide insight into both overall performance and class-wise behavior, which is critical for defect-sensitive applications.

## 🚀Edge Deployment Considerations

From the early stages of development, model portability and deployment compatibility are considered. The trained model is exported to the ONNX format to enable integration with the NXP eIQ toolchain.

Key edge considerations include:
- Compatibility with NXP i.MX RT series devices
- Low memory and compute requirements
- Feasibility of real-time inference







