# Trained Models

This directory contains trained model artifacts prepared for edge deployment.

## Model Variants

- **Unquantized ONNX Model**
  - Higher numerical precision
  - Used as a performance reference
  - Suitable for validation and benchmarking

- **Quantized ONNX Model**
  - Reduced model size and memory footprint
  - Optimized for edge deployment
  - Compatible with NXP eIQ workflows

## Edge Deployment Context

The availability of both quantized and unquantized models enables systematic evaluation of accuracy vs efficiency trade-offs, which is critical for deployment on resource-constrained edge devices such as the NXP i.MX RT series.
