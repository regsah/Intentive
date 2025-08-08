import './styles/ColumnChooser.css'

function ColumnChooser({openStates, setOpenStates})
{
    function toggleColumn(column) {
        if (openStates[column]) {
            let closedCount = 0;
            let totalCount = 0;

            for (const key in openStates) {
                if (!openStates[key]) closedCount++;
                totalCount++;
            }

            if (closedCount === totalCount - 1) return;
        }

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
                    onClick={() => toggleColumn(key)}
                    key={key}>
                        {key}
                    </div>
                );
            })}
        </div>
    )

}

export default ColumnChooser;