import DataTable from '../components/DataTable';
import { useState } from 'react';
import './DashboardPage.css';

function DashboardPage() {
    const [openStates, setOpenStates] = useState({
        id: true, type: false, query: true, intent: true, emotion: true,
    });

    return (
        <div className="DashboardPage-container">
            <DataTable openStates={openStates}/>
        </div>
    );
}

export default DashboardPage;