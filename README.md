# Intrusion Detection Dashboard

### This web app is an interactive dashboard that allows users to explore network session data and predict whether a session is likely to be a cyberattack. The prediction is powered by a LightGBM machine learning model, trained on an intrusion detection dataset and deployed via a Flask AP on Hugging Face Spaces.

## Live Demo

- Streamlit Dashbboard
- Prediction API
- Model Notebook

## Model Info

## | Model | Recall | Precision | F1 Score | Threshold |

## | LightGBM | 87.1% | 62.8% | 73.0% | 0.2 |

## Features

- Interactive Filtering: View attack distributions by protocol and encryption type.
- Visualization: Explore traffic patterns and protocol frequency.
- Real-time Prediction: Input session characteristics to predict if it's likely an intrusion.
- API Integration: Connects to a Flask API deployed on Hugging Face Spaces.
