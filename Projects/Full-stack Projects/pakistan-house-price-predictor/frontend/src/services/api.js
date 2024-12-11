import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

export const predict = async (formData) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/predict/`, formData);
        return response.data.prediction;
    } catch (error) {
        console.error('Error during prediction:', error);
        throw error;
    }
};