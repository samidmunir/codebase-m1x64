import {useEffect, useState} from 'react';
import JobCard from '../components/JobCard';
import {getJobs} from '../services/jobService';

const Home = () => {
    const [jobs, setJobs] = useState([]);

    useEffect(() => {
        const fetchJobs = async () => {
            const data = await getJobs();
            setJobs(data);
        };

        fetchJobs();
    }, []);

    return (
        <div className='container mx-auto py-6'>
            <h1 className='text-2xl font-bold text-center mb-6'>Job Applications</h1>
            <div className='grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4'>
                {jobs.map(job => (
                    <JobCard key={job.id} {...job} />
                ))}
            </div>
        </div>
    );
};

export default Home;