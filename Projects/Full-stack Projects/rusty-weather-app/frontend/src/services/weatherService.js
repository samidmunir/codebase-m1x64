import axios from 'axios';

const API_BASE_URL = 'http://localhost:8080'; // Rust backend

export const fetchWeather = async (location) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/weather/${location}`);
        return response.data;
    } catch (error) {
        console.error("Error fetching weather data: ", error);
        throw error;
    }
};