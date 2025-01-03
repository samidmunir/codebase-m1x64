import {useState} from 'react';
import {createJob} from '../services/jobService';

const AddJob = () => {
    const [formData, setFormData] = useState({
        title: '',
        company: '',
        status: '',
        applied_date: '',
        notes: '',
    });

    const handleChange = (e) => {
        setFormData({...formData, [e.target.name]: e.target.value});
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        await createJob(formData);
        alert('Job added successfully!');
    };

    return (
        <form className='max-w-md mx-auto p-4 bg-white shadow-md rounded' onSubmit={handleSubmit}>
            <h2 className='text-xl font-bold mb-4'>Add Job</h2>
            {['title', 'company', 'status', 'applied_date', 'notes'].map(field => (
                <div key={field} className='mb-3'>
                    <label className='block text-gray-600 mb-1' htmlFor={field}>
                        {field.replace('_', ' ').toUpperCase()}
                    </label>
                    <input
                        type={field === 'applied_date' ? 'date': 'text'}
                        name={field}
                        id={field}
                        value={formData[field]}
                        onChange={handleChange}
                        className='w-full border px-3 py-2 rounded'
                        required={field !== 'notes'}
                    />
                </div>
            ))}
            <button type='submit' className='bg-blue-500 text-white px-4 py-2 rounded'>Add Job</button>
        </form>
    );
};

export default AddJob;