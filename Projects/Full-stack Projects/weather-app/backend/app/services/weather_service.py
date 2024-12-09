import httpx
from app.core.config import settings

BASE_URL = 'http://api.weatherstack.com'

async def fetch_current_weather(city: str):
    params = {
        'access_key': settings.weatherstack_api_key,
        'query': city,
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{BASE_URL}/current', params = params)
        response.raise_for_status()
        
        return response.json()