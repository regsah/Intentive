import './styles/DataTable.css';
import DataRow from './DataRow';
import { useState, useEffect } from 'react';
import axios from 'axios';

function DataTable() {
    const [openStates, setOpenStates] = useState({
        id: true, type: true, query: true, intent: true, emotion: true,
    });

    const [data, setData] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/fetch_entries', {
            params: {intent_label: null, emotion_label: null, type_label: null }
        }).then(response => {
            setData(response.data.data);
        }).catch(error => {
            if (error.response) console.error("Error:", error.response.status, error.response.data);
            else console.error("Error:", error.message);
        });
    }, []);


    return (
        <div className="DataTable-container">
            <div className="DataTable-header">
                {Object.keys(openStates).map((key) => (
                    <div key={key} className="DataTable-header-item"> {key} </div>
                ))}
            </div>
            <div className="DataTable-body">
                {data.map((rowData, index) => (
                    <DataRow key={index} rowData={rowData} openStates={openStates} />
                ))}
            </div>
        </div>    
    )

    /*
    return (
        <div className="DataTable-container">
            {openStates.id && <DataColumn column={{ width: '200px', name:'id' }} data={data.map(d => d.id)} />}
            {openStates.type && <DataColumn column={{ width: '100px', name:'type' }} data={data.map(d => d.type)} />}
            {openStates.query && <DataColumn column={{ width: '300px', name:'query' }} data={data.map(d => d.query)} />}
            {openStates.intent && <DataColumn column={{ width: '150px', name:'intent' }} data={data.map(d => d.intent)} />}
            {openStates.emotion && <DataColumn column={{ width: '150px', name:'emotion' }} data={data.map(d => d.emotion)} />}
        </div>
    );
    */
}

export default DataTable;