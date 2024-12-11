from app.utils.model_loader import load_model
import numpy as np

# Load the model once at startup
model = load_model('data/random_forest_model.pkl')

def make_prediction(data):
    features = np.array([[
        data.bedrooms, data.baths, data.size, data.bed_bath_ratio,
        data.price_per_sqft, data.total_rooms, data.luxury_index,
        data.FECHS_2, data.Attock, data.Faisalabad, data.Gujranwala,
        data.Islamabad, data.Karachi, data.Lahore, data.Multan,
        data.Murree, data.Peshawar, data.Quetta, data.Rawalpindi
    ]])
    
    return float(model.predict(features)[0])