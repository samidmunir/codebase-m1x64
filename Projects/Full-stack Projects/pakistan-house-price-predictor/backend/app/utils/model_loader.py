import joblib

def load_model(filepath):
    return joblib.load(filepath)