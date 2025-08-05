import DataTable from '../components/DataTable';
import { useEffect, useState } from 'react';
import './DashboardPage.css';
import ColumnChooser from '../components/ColumnChooser';
import ColumnFilter from '../components/ColumnFilter';

function DashboardPage() {
    const [openStates, setOpenStates] = useState({
        id: true, type: false, query: true, intent: true, emotion: true,
    });

    const [filters, setFilters] = useState({
        type_label: null, intent_label: null, emotion_label: null 
    });

    return (
        <div className="DashboardPage-container">
            <div className='Dashboard-container'>
                <div className="Dashboard-upper-bar-container">
                    <ColumnChooser openStates={openStates} setOpenStates={setOpenStates}/>
                    <ColumnFilter filters={filters} setFilters={setFilters} />
                </div>
                <DataTable openStates={openStates} filters={filters}/>            
            </div>
        </div>
    );
}

export default DashboardPage;