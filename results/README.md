# Model Evaluation Results

This section summarizes the performance of the trained defect detection model. Since the task is formulated as a **detection-based defect classification problem**, evaluation is performed using standard object detection metrics.

## 📊Quantitative Results

| Metric | Value | Description |
|------|------|------------|
| mAP@50 | **0.9288** | Mean Average Precision at IoU = 0.5 |
| mAP@50–95 | **0.7483** | Mean AP averaged over IoU thresholds (0.5–0.95) |
| Precision | **0.9081** | Fraction of correct detections among all detections |
| Recall | **0.8963** | Fraction of detected defects among all ground truth defects |

## 🧠Interpretation

The high mAP@50 score indicates strong defect localization and classification capability, while the mAP@50–95 score reflects robust performance across stricter localization thresholds. Balanced precision and recall values demonstrate that the model avoids both excessive false positives and missed defects, which is critical for semiconductor inspection workflows.

