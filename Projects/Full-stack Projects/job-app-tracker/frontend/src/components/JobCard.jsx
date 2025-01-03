/* eslint-disable react/prop-types */
const JobCard = ({id, title, company, link, status, applied_date, notes, onDelete}) => (
    <div className='bg-white shadow rounded p-4 m-2'>
        <h2 className='text-xl font-semibold'>{title}</h2>
        <p className='text-sm text-gray-600'>{company}</p>
        <p className='text-sm text-blue-600'>{link}</p>
        <p>Status: <span className='font-medium'>{status}</span></p>
        <p>Applied: {applied_date}</p>
        {notes && <p>Notes: {notes}</p>}
        <button className='text-red-500 mt-2' onClick={() => onDelete(id)}>Delete</button>
    </div>
);

export default JobCard;