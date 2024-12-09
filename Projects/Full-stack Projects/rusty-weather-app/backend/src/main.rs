use actix_cors::Cors;
use actix_web::{get, web, App, HttpServer, Responder};
use reqwest::Client;
use serde::Deserialize;

#[derive(Deserialize)]
struct WeatherResponse {
    current: CurrentWeather,
}

#[derive(Deserialize)]
struct CurrentWeather {
    temperature: i32,
    weather_descriptions: Vec<String>,
}

#[get("/weather/{location}")]
async fn get_weather(location: web::Path<String>, client: web::Data<Client>) -> impl Responder {
    let api_key = "5158b595c86e5dcd63889dc6d3605246";
    let url = format!(
        "http://api.weatherstack.com/current?access_key={}&query={}",
        api_key,
        location
    );

    match client.get(&url).send().await {
        Ok(response) => {
            if let Ok(weather) = response.json::<WeatherResponse>().await {
                format!(
                    "Current temperature in {} is {}°C with {}.",
                    location,
                    weather.current.temperature,
                    weather.current.weather_descriptions.join(", ")
                )
            } else {
                "Failed to parse weather data.".to_string()
            }
        }
        Err(_) => "Failed to fetch weather data.".to_string(),
    }
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    println!("\nRusty Weather App <backend>");
    println!("-----------------------------\n");

    println!("\trusty-weather-app <backend> listening...");

    let client = Client::new();

    HttpServer::new(move || {
        let cors = Cors::default()
            .allow_any_origin()
            .allow_any_method()
            .allow_any_header();

        App::new()
            .wrap(cors)
            .app_data(web::Data::new(client.clone()))
            .service(get_weather)
    })
    .bind("localhost:8080")?
    .run()
    .await
}