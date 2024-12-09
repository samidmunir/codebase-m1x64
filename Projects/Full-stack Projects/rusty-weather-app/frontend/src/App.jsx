import {useState} from 'react';
import { fetchWeather } from './services/weatherService';

const App = () => {
  const [location, setLocation] = useState('');
  const [weather, setWeather] = useState(null);
  const [error, setError] = useState('');

  const handleFetchWeather = async () => {
    setError('');
    try {
      const data = await fetchWeather(location);
      setWeather(data);
      // console.log(data);
    } catch {
      setError('Failed to fetch weather data. Please try again.');
    }
  }

  return (
    <div>
      <h1>Weather App</h1>
      <input
        type='text'
        placeholder='Enter location'
        value={location}
        onChange={(e) => setLocation(e.target.value)}
      />
      <button onClick={handleFetchWeather}>
        Get Weather
      </button>
      {
        weather && (
          <div>
            <h2>Weather in {location}</h2>
            <p>{weather}</p>
            {/* <p>Temperature: {weather.split('is')[1].split('°')[0]}°C</p> */}
          </div>
        )
      }
      {error && <p>{error}</p>}
    </div>
  );
};

export default App;