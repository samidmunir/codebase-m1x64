from supabase import create_client
import os as OS
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = OS.getenv('SUPABASE_URL')
SUPABASE_KEY = OS.getenv('SUPABASE_KEY')
supabase = create_client(supabase_url = SUPABASE_URL, supabase_key = SUPABASE_KEY)