// import axios from 'axios'
import API from '../api';

const API_URL = 'http://localhost:8000/api';

export const getJobs = async () => {
    const response = await API.get(`${API_URL}/jobs`);
    return response.data;
};

export const getJobById = async (id) => {
    const response = await API.get(`${API_URL}/jobs/${id}`);
    return response.data;
}

export const createJob = async (jobData) => {
    const response = await API.post(`${API_URL}/jobs`, jobData);
    return response.data;
};

export const updateJob = async (id, jobData) => {
    const response = await API.put(`${API_URL}/jobs/${id}`, jobData);
    return response.data;
};

export const deleteJob = async (id) => {
    const response = await API.delete(`${API_URL}/jobs/${id}`);
    return response.data;
};