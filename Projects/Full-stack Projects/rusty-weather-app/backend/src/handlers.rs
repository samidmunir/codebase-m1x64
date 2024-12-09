use actix_web::{get, web, HttpResponse, Responder};
use crate::services;
use crate::utils::AppError;

#[get("/weather/{location}")]
async fn get_weather(location: web::Path<String>) -> impl Responder {
    match services::fetch_weather(&location).await {
        Ok(weather) => HttpResponse::Ok().json(weather),
        Err(err) => err.error_response(),
    }
}

pub fn init_routes(cfg: &mut web::ServiceConfig) {
    cfg.service(get_weather);
}