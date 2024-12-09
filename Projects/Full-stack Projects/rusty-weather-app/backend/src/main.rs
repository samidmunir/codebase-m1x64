mod handlers;
mod services;
mod models;
mod utils;

use actix_web::{App, HttpServer};

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    println!("\nStarting serve on http://localhost:8080");

    HttpServer::new(|| {
        App::new().configure(handlers::init_routes)
    })
    .bind("localhost:8080")?
    .run()
    .await
}