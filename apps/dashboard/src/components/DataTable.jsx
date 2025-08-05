import './styles/DataTable.css';
import DataRow from './DataRow';
import { useState, useEffect } from 'react';
import axios from 'axios';

function DataTable({openStates, filters}) {
    const [data, setData] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/fetch_entries', {
            params: {
                intent_label: filters.intent_label, 
                emotion_label: filters.emotion_label, 
                type_label: filters.type_label 
            }
        }).then(response => {
            setData(response.data.data);
        }).catch(error => {
            if (error.response) console.error("Error:", error.response.status, error.response.data);
            else console.error("Error:", error.message);
        });
    }, [filters]);


    return (
        <div className="DataTable-container">
            <div className="DataTable-header">
                {Object.keys(openStates).map((key) => (
                    openStates[key] && <div key={key} className="DataTable-header-item"> {key} </div>
                ))}
            </div>
            <div className="DataTable-body">
                {data.map((rowData, index) => (
                    <DataRow key={index} rowData={rowData} openStates={openStates} />
                ))}
            </div>
        </div>    
    )
}

export default DataTable;