# ml_models.py
import os
import joblib
from tensorflow import keras
import numpy as np

# Paths to models
MODEL_DIR = os.path.join(os.path.dirname(__file__), 'ml_models')
FEAT_MODEL_PATH = os.path.join(MODEL_DIR, 'feat_extractor.keras')
CLASSIFIER_PATH = os.path.join(MODEL_DIR, 'agri_classifier.pkl')

feat_extractor = keras.models.load_model(FEAT_MODEL_PATH)
clf = joblib.load(CLASSIFIER_PATH)

IMG_SIZE = (224, 224)

def predict_agri(img_path, threshold=0.6):
    """Predict if the uploaded image is agricultural equipment"""
    img = keras.preprocessing.image.load_img(img_path, target_size=IMG_SIZE)
    arr = keras.preprocessing.image.img_to_array(img)
    arr = np.expand_dims(arr, 0)
    arr = keras.applications.mobilenet_v2.preprocess_input(arr)

    feat = feat_extractor.predict(arr, verbose=0)
    prob = clf.predict_proba(feat)[0][1]
    label = 'agri' if prob >= threshold else 'not_agri'
    return label, prob
