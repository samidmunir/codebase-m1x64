from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import jobs

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

app.include_router(jobs.router, prefix = '/api', tags = ['Jobs'])

@app.get('/')
def read_root():
    return {'message': 'Welcome to Job-App-Tracker Backend!'}