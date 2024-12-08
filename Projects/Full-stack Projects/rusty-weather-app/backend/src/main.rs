use actix_web::{get, web, App, HttpServer, Responder};
use reqwest::Client;
use serde::Deserialize;
use std::env;

#[derive(Deserialize)]
struct WeatherResponse {
    current: CurrentWeather,
}

#[derive(Deserialize)]
struct CurrentWeather {
    temperature: i32,
    weather_descriptions: Vec<String>,
}

fn main() {
    println!("\nRusty Weather App <backend>");
    println!("-----------------------------\n");
}