from utils.database import supabase
from models.job import Job

class JobService:
    @staticmethod
    def get_all_jobs():
        response = supabase.table('jobs').select('*').execute()
        return response.data
    
    @staticmethod
    def get_job_by_id(job_id: str):
        response = supabase.table('jobs').select('*').eq('id', job_id).execute()
        if response.data:
            return response.data[0]
        return None
    
    @staticmethod
    def create_job(job: Job):
        response = supabase.table('jobs').insert(job.model_dump()).execute()
        if response.error:
            raise ValueError(response.error.message)
        return response.data
    
    @staticmethod
    def update_job(job_id: str, job: Job):
        response = supabase.table('jobs').update(job.model_dump()).eq('id', job_id).execute()
        if response.error or not response.data:
            return None
        return response.data[0]
    
    @staticmethod
    def delete_job(job_id: str):
        response = supabase.table('jobs').delete().eq('id', job_id).execute()
        return not response.error