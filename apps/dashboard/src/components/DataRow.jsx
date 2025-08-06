import { useEffect, useState } from 'react';
import './styles/DataRow.css';
import { MdDelete } from "react-icons/md";
import axios from 'axios';

function DataRow({ rowData, openStates, handleDeletion }) {

    return (
        <div className="DataRow-container">
            {Object.keys(openStates).map((key) => (
                openStates[key] && (
                    <div key={key} className="DataRow-item">
                        {rowData[key]}
                    </div>
                )
            ))}
            <div className="DataRow-delete" onClick={() => handleDeletion(rowData.id)}><MdDelete /></div>
        </div>
    );
}

export default DataRow;