import {useState} from 'react';
import SearchBar from '../components/SearchBar';
import WeatherCard from '../components/WeatherCard';

const Home = () => {
    const [weather, setWeather] = useState(null);

    const fetchWeather = async (city) => {
        try {
            const response = await fetch(`http://localhost:8000/api/v1/current_weather?city=${city}`)
            const data = await response.json();
            setWeather({
                city: data.data.location.name,
                temperature: data.data.current.temperature,
                condition: data.data.current.weather_descriptions[0],
            });
        } catch (error) {
            console.error('Error fetching weather:', error);
        }
    };

    return (
        <div className='p-4'>
            <SearchBar onSearch={fetchWeather} />
            {weather && <WeatherCard weather={weather} />}
        </div>
    )
};

export default Home;