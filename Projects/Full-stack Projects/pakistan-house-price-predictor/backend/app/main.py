from fastapi import FastAPI
from app.routers import prediction

app = FastAPI(
    title = 'PAK House Prediction API',
    description = 'API for predicting Pakistan House Prices',
    version = '1.0.0'
)

app.include_router(prediction.router)

@app.get('/')
async def root():
    return {'message': 'Welcome to the PAK House Prediction API!'}