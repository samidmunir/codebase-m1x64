from fastapi import APIRouter, HTTPException
from app.services.weather_service import fetch_current_weather

router = APIRouter()

@router.get('/current_weather')
async def get_current_weather(city: str):
    try:
        data = await fetch_current_weather(city)
        return {'data': data}
    except Exception as e:
        raise HTTPException(status_code = 400, detail = str(e))