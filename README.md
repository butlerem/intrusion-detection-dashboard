# Intrusion Detection Dashboard

## Overview
An interactive Streamlit app for visualizing network session data and predicting cyberattacks using a LightGBM model. The model backend is served via a Flask API hosted on Hugging Face Spaces. Enables real-time intrusion prediction based on session characteristics, interactive filtering and visualization of network traffic, and an API-backed model inference using a threshold-optimized LightGBM classifier.

## Model Details
- **Model**: LightGBM Classifier
- **Threshold**: 0.2 (favoring recall over precision)
- **Recall**: 87.1%  
- **Precision**: 62.5%  
- **F1 Score**: 73.0%

## Features
- **Interactive Prediction**: Input session data and receive real-time attack predictions.
- **Visual Insights**: Explore traffic patterns by protocol, encryption type, and more.
- **API Integration**: Live inference powered by a deployed Flask API.
- **Custom Threshold**: Lowered to detect more attacks at the expense of precision.

## Links
- [Try the Dashboard](https://huggingface.co/spaces/e-eeeema/intrusion-dashboard)
- [Model Training Notebook](https://github.com/butlerem/intrusion-detection-model-lgbm/blob/main/intrusion_detector.ipynb)
- [Dataset on Kaggle](https://www.kaggle.com/datasets/sampadab17/network-intrusion-detection/code)

## Example API Request

```bash
curl -X POST https://e-eeeema-intrusion-detection.hf.space/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [500, 3, 500.0, 0.5, 1, 0, 1, 0, 0, 1]}'
```
## License
MIT
