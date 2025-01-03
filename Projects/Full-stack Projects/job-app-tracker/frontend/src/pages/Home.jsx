import {useEffect, useState} from 'react';
import API from '../api';
import JobCard from '../components/JobCard';

const Home = () => {
    const [jobs, setJobs] = useState([]);

    useEffect(() => {
        API.get('/jobs').then(response => setJobs(response.data));
    }, []);

    const handleDelete = async (id) => {
        await API.delete(`/jobs/${id}`);
        setJobs(jobs.filter(job => job.id !== id));
    };

    return (
        <div className='container mx-auto py-6'>
            <h1 className='text-2xl font-bold text-center mb-6'>Job Applications</h1>
            <div className='grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4'>
                {jobs.map(job => (
                    <JobCard key={job.id} {...job} onDelete={handleDelete} />
                ))}
            </div>
        </div>
    );
};

export default Home;