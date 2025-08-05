import DataTable from '../components/DataTable';
import { useState } from 'react';
import './DashboardPage.css';
import ColumnChooser from '../components/ColumnChooser';

function DashboardPage() {
    const [openStates, setOpenStates] = useState({
        id: true, type: false, query: true, intent: true, emotion: true,
    });

    return (
        <div className="DashboardPage-container">
            <div className='Dashboard-container'>
                <ColumnChooser openStates={openStates} setOpenStates={setOpenStates}/>
                <DataTable openStates={openStates}/>            
            </div>
        </div>
    );
}

export default DashboardPage;