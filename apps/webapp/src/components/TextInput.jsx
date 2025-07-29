import React, { useState } from 'react';

import { MdKeyboardVoice } from "react-icons/md";
import { FaArrowUp } from "react-icons/fa";
import './styles/TextInput.css'

function TextInput() {
    function handleSubmit(query, setQuery) {
        console.log('Submitted query:', query);
        setQuery('');
    }

    const [query, setQuery] = useState('');

    return (
        <div className="TextInput-container">
            <textarea 
                className="TextInput-field"
                placeholder="Type your query..."
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                rows={4}
            />
            <div className="TextInput-buttonbar">
                <button className="TextInput-button TextInput-button-left"> <MdKeyboardVoice /> </button>
                <button className="TextInput-button TextInput-button-right" 
                        onClick={() => handleSubmit(query, setQuery)}>
                    <FaArrowUp />
                </button>
            </div>

        </div>
    )
}

export default TextInput; 