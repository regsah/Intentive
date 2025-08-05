import { useEffect, useState } from 'react';
import axios from 'axios';
import './styles/ColumnFilter.css'
function ColumnFilter({ filters, setFilters }) {
    const [filterLists, setFilterLists] = useState({});

    const fetchFromBackend = async (endpoint) => {
        try {
            const response = await axios.get(`http://localhost:8000/api/${endpoint}`);
            return response.data.data;
        } catch (error) {
            console.error(`Error fetching from ${endpoint}:`, error);
            throw error;
        }
    };

    useEffect(() => {
        const fetchFilters = async () => {
            const newFilterLists = {};
            for (const key in filters) {
                newFilterLists[key] = await fetchFromBackend(`fetch_${key}`);
            }
            setFilterLists(newFilterLists);
        };

        fetchFilters();
    }, [filters]);

    const handleChange = (key, event) => {
        const value = event.target.value === "" ? null : event.target.value;
        setFilters((prev) => ({
            ...prev,
            [key]: value,
        }));
    };

    return (
        <div className="ColumnFilter-container">
        {Object.keys(filters).map((key) => {
            return (
                <div key={key} className="ColumnFilter-dropdown">
                    <select
                        style={{ width: '100%' }}
                        value={filters[key] ?? ""}
                        onChange={(e) => handleChange(key, e)}
                    >
                        <option value="">All</option>
                        {(filterLists[key] || []).map((option, idx) => (
                            <option key={`${key}-${option}-${idx}`} value={option}>
                                {option}
                            </option>
                        ))}
                    </select>   
                </div>
        )})}
        </div>
    );
}

export default ColumnFilter;