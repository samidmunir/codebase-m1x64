import {Link} from 'react-router-dom';

const Navbar = () => (
    <nav className='bg-gray-800 text-white p-4'>
        <div className='container mx-auto flex justify-between'>
            <Link to='/' className='text-xl font-bold'>Job App Tracker</Link>
            <div>
                <link to='/' className='mr-4'>Home</link>
                <link to='/add-job' className='mr-4'>Add Job</link>
            </div>
        </div>
    </nav>
);

export default Navbar;