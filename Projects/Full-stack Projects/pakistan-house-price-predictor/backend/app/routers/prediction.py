from fastapi import APIRouter
from app.models import PredictionRequest
from app.services import make_prediction

router = APIRouter(
    prefix = '/predict',
    tags = ['Prediction']
)

@router.post('/')
async def predict(data: PredictionRequest):
    prediction = make_prediction(data)
    return {'prediction': prediction}
