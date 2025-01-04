from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
import json as JSON

DATA_FILE_PATH = '../app/data/data.json'

def save_tasks_to_file():
    with open(DATA_FILE_PATH, 'w') as file:
        JSON.dump([task.dict() for task in tasks], file, indent = 4)

def load_tasks_from_file():
    global tasks
    try:
        with open(DATA_FILE_PATH, 'r') as file:
            tasks_data = JSON.load(file)
            tasks = [Task(**task) for task in tasks_data]
    except FileNotFoundError:
        tasks = []

app = FastAPI(on_startup = [load_tasks_from_file])

@app.on_event('startup')
async def startup_event():
    load_tasks_from_file()

class Task(BaseModel):
    id: Optional[UUID] = None
    title: str
    company: str
    link: str
    status: str
    applied_date: str
    description: Optional[str] = None
    notes: Optional[str] = None

tasks = []

@app.post('/tasks/', response_model = Task)
async def create_task(task: Task):
    task.id = uuid4()
    tasks.append(task)
    save_tasks_to_file()
    return task

@app.get('/tasks/', response_model = List[Task])
async def get_tasks():
    return tasks

@app.get('/tasks/{task_id}', response_model = Task)
async def get_task(task_id: UUID):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code = 404, detail = 'Task not found.')

@app.put('/tasks/{task_id}', response_model = Task)
async def update_task(task_id: UUID, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = task.copy(update = updated_task.dict(exclude_unset = True))
            tasks[index] = updated_task
            # save_tasks_to_file()
            return updated_task
    raise HTTPException(status_code = 404, detail = 'Task not found.')

@app.delete('/tasks/{task_id}', response_model = Task)
async def delete_task(task_id: UUID):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            deleted_task = tasks.pop(index)
            # save_tasks_to_file()
            return deleted_task
    raise HTTPException(status_code = 404, detail = 'Task not found.')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host = 'localhost', port = 8000)