use crate::models::WeatherResponse;
use crate::utils::AppError;
use reqwest::Client;

const API_BASE_URL: &str = "http://api.weatherstack.com/current";
const API_KEY: &str = "5158b595c86e5dcd63889dc6d3605246";

pub async fn fetch_weather(location: &str) -> Result<WeatherResponse, AppError> {
    let url = format!("{}?access_key={}&query={}", API_BASE_URL, API_KEY, location);
    let client = Client::new();

    let response = client.get(&url).send().await.map_err(AppError::ReqwestError)?;
    let weather = response.json::<WeatherResponse>().await.map_err(AppError::ReqwestError)?;
    Ok(weather)
}