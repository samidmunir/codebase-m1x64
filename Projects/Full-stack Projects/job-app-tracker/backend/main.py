from fastapi import FastAPI
from supabase import create_client, Client
from dotenv import load_dotenv
import os as OS

load_dotenv()

app = FastAPI()

SUPABASE_URL = OS.getenv('SUPABASE_URL')
SUPABASE_KEY = OS.getenv('SUPABASE_KEY')
supabase: Client = create_client(supabase_url = SUPABASE_URL, supabase_key = SUPABASE_KEY)

@app.get('/')
def read_root():
    return {'message': 'Welcome to Job-App-Tracker Backend!'}

@app.get('/jobs')
def get_jobs():
    response = supabase.table('jobs').select('*').execute()
    return response.data