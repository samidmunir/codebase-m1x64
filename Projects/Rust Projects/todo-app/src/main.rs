use clap::{Parser, Subcommand};
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize, Debug)]
struct Task {
    id: usize,
    description: String,
    done: bool,
}

#[derive(Parser)]
#[command(name = "Todo App")]
#[command(about = "A simple command-line to-do list app", long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    Add {description: String},
    List,
    Done {id: usize},
    Remove {id: usize},
}

fn main() {
    println!("\nRusty Todo App\n");
}