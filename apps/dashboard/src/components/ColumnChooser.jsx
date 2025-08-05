import './styles/ColumnChooser.css'

function ColumnChooser({openStates, setOpenStates})
{
    function toggleColumn(column) {
        setOpenStates({
            ...openStates,
            [column]: !openStates[column]
        })
    }

    return (
        <div className="ColumnChooser-container">
            {Object.keys(openStates).map((key) => {
                return (
                    <div className={`columnState-button ${!openStates[key] && 'columnState-button-off'}`}
                    onClick={() => toggleColumn(key)}>
                        {key}
                    </div>
                );
            })}
        </div>
    )

}

export default ColumnChooser;