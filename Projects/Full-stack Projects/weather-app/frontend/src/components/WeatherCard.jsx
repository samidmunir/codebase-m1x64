const WeatherCard = (weather) => (
    <div className='bg-gray-100 p-4 rounded shadow'>
        <h2 className='text-lg font-bold'>{weather.city}</h2>
        <p>Temperature: {weather.temperature}°C</p>
        <p>Condition: {weather.condition}</p>
    </div>
);

export default WeatherCard;