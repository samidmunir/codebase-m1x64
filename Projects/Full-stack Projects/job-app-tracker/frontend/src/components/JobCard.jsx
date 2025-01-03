const JobCard = ({title, company, status, applied_date, notes}) => (
    <div className='bg-white shadow rounded p-4 m-2'>
        <h2 className='text-xl font-semibold'>{title}</h2>
        <p className='text-sm text-gray-600'>{company}</p>
        <p>Status: <span className='font-medium'>{status}</span></p>
        <p>Applied: {applied_date}</p>
        {notes && <p>Notes: {notes}</p>}
    </div>
);

export default JobCard;