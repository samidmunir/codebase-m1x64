import {useState} from 'react';

// eslint-disable-next-line react/prop-types
const SearchBar = ({onSearch}) => {
    const [city, setCity] = useState('');

    const handleSearch = () => {
        if (city) onSearch(city);
    };

    return (
        <div className='flex items-center space-x-2'>
            <input
                type='text'
                placeholder='Enter city'
                value={city}
                onChange={(e) => setCity(e.target.value)}
                className='border p-2 rounded'
            />
            <button
                onClick={handleSearch}
                className='bg-blue-500 text-white px-4 py-2 rounded'
            >
                Search
            </button>
        </div>
    );
};

export default SearchBar;