use clap::Parser;
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize, Debug)]
struct Task {
    id: usize,
    description: String,
    done: bool,
}

#[derive(clap::Parser)]
#[clap(name = "Todo App")]
#[clap(about = "A simple command-line to-do list app", long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(clap::Subcommand)]
enum Commands {
    Add {description: String},
    List,
    Done {id: usize},
    Remove {id: usize},
}

fn add_task(tasks: &mut Vec<Task>, description: String) {
    let id = tasks.len() + 1;
    tasks.push(Task {
        id,
        description,
        done: false,
    });
}

fn save_tasks(tasks: &Vec<Task>, filename: &str) -> Result<(), std::io::Error> {
    let data = serde_json::to_string_pretty(tasks)?;
    std::fs::write(filename, data)?;
    Ok(())
}

fn load_tasks(filename: &str) -> Vec<Task> {
    if let Ok(data) = std::fs::read_to_string(filename) {
        serde_json::from_str(&data).unwrap_or_else(|_| Vec::new())
    } else {
        Vec::new()
    }
}

fn list_tasks(tasks: &Vec<Task>) {
    for task in tasks {
        println!(
            "{}: [{}] {}",
            task.id,
            if task.done {"X"} else {" "},
            task.description
        );
    }
}

fn mark_done(tasks: &mut Vec<Task>, id: usize) {
    if let Some(task) = tasks.iter_mut().find(|t| t.id == id) {
        task.done = true;
        println!("Task {} marked as done.", id);
    } else {
        println!("Task with ID {} not found.", id);
    }
}

fn remove_task(tasks: &mut Vec<Task>, id: usize) {
    if let Some(pos) = tasks.iter().position(|t| t.id == id) {
        tasks.remove(pos);
        println!("Task {} removed.", id);
    } else {
        println!("Task with ID {} not found.", id);
    }
}

fn main() {
    println!("\nRusty Todo App\n");

    let filename = "tasks.json";
    let mut tasks = load_tasks(filename);

    let cli = Cli::parse();

    match cli.command {
        Commands::Add {description} => {
            add_task(&mut tasks, description);
        }

        Commands::List => {
            list_tasks(&tasks);
        }

        Commands::Done {id} => {
            mark_done(&mut tasks, id);
        }

        Commands::Remove {id} => {
            remove_task(&mut tasks, id);
        }
    }

    if let Err(e) = save_tasks(&tasks, filename) {
        eprintln!("Error saving tasks: {}", e);
    }
}