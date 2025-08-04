import './styles/DataColumn.css';

function DataColumn({ column }) {
    let style = {
        width: column.width,
    }

    return (
        <div className="DataColumn-container" style={style}>
            <div className='DataColumn-header'>{column.name}</div>
        
        </div>
    );
}

export default DataColumn;