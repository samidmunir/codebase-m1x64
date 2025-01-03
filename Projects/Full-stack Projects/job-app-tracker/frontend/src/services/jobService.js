import axios from 'axios'

const API_URL = 'http://localhost:8000';

export const getJobs = async () => {
    const response = await axios.get(`${API_URL}/jobs`);
    return response.data;
};

export const createJob = async (jobData) => {
    const response = await axios.post(`${API_URL}/jobs`, jobData);
    return response.data;
};