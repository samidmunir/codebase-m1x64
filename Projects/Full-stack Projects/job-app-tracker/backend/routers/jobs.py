from fastapi import APIRouter, HTTPException
from models.job import Job
from services.job_service import JobService

router = APIRouter()

@router.get('/jobs')
def get_jobs():
    return JobService.get_all_jobs()

@router.get('/jobs/{job_id}')
def get_job(job_id: str):
    job = JobService.get_job_by_id(job_id)
    if not job:
        raise HTTPException(status_code = 404, detail = 'Job not found.')
    return job

@router.post('/jobs')
def create_job(job: Job):
    return JobService.create_job(job)

@router.put('/jobs/{job_id}')
def update_job(job_id: str, job: Job):
    updated_job = JobService.update_job(job_id, job)
    if not updated_job:
        raise HTTPException(status_code = 404, detail = 'Job not found.')
    
@router.delete('/jobs/{job_id}')
def delete_job(job_id: str):
    if not JobService.delete_job(job_id):
        raise HTTPException(status_code = 404, detail = 'Job not found.')
    return {'message': 'Job deleted successfully.'}