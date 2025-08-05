import { useEffect, useState } from 'react';
import './styles/DataRow.css';

function DataRow({ rowData, openStates }) {
    useEffect(() => {
        console.log(`DataRow mounted with data: ${JSON.stringify(rowData)}`);
    }, [rowData]);

    return (
        <div className="DataRow-container">
            {Object.keys(rowData).map((key) => (
                openStates[key] && <div key={key} className="DataRow-item">{rowData[key]}</div>
            ))}
        </div>
    );
}

export default DataRow;