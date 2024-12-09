use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Debug)]
pub struct WeatherResponse {
    pub location: Location,
    pub current: CurrentWeather,
}

#[derive(Serialize, Deserialize, Debug)]
pub struct Location {
    pub name: String,
    pub country: String,
    pub region: String,
    pub lat: String,
    pub lon: String,
    pub localtime: String,
}

#[derive(Serialize, Deserialize, Debug)]
pub struct CurrentWeather {
    pub temperature: i32,
    pub feelslike: i32,
    pub weather_descriptions: Vec<String>,
    pub wind_speed: i32,
    pub wind_degree: i32,
    pub wind_dir: String,
    pub pressure: i32,
    pub precip: f64,
    pub humidity: i32,
    pub cloudcover: i32,
    pub uv_index: i32,
    pub visibility: i32,
}