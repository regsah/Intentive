import './styles/DataTable.css';
import DataColumn from './DataColumn';

function DataTable() {
    return (
        <div className="DataTable-container">
            <DataColumn column={{ width: '200px', name:'id' }} />
            <DataColumn column={{ width: '200px', name:'query' }} />
            <DataColumn column={{ width: '200px', name:'type' }} />
            <DataColumn column={{ width: '200px', name:'intent' }} />
            <DataColumn column={{ width: '200px', name:'emotion' }} />
        </div>
    );
}

export default DataTable;