use actix_web::{HttpResponse, ResponseError};
use std::fmt;

#[derive(Debug)]
pub enum AppError {
    ReqwestError(reqwest::Error),
    Other(String),
}

impl fmt::Display for AppError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            AppError::ReqwestError(err) => write!(f, "Request error: {}", err),
            AppError::Other(msg) => write!(f, "Error: {}", msg),
        }
    }
}

impl ResponseError for AppError {
    fn error_response(&self) -> HttpResponse {
        match self {
            AppError::ReqwestError(_) => {
                HttpResponse::InternalServerError().body("Failed to fetch data from external API.")
            }
            AppError::Other(msg) => HttpResponse::InternalServerError().body(msg),
        }
    }
}

pub fn handle_error<E: ResponseError>(err: E) -> HttpResponse {
    HttpResponse::InternalServerError().body(format!("Error: {}", err))
}