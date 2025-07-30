import React, { useState } from 'react';

import { MdKeyboardVoice } from "react-icons/md";
import { FaArrowUp } from "react-icons/fa";
import { GiCancel } from "react-icons/gi";
import { FaPause } from "react-icons/fa6";


import './styles/TextInput.css'

function TextInput({isRecording, setIsRecording}) {
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
                {
                    isRecording ? (
                        <div className="TextInput-left-buttons-container">
                            <button className="TextInput-button TextInput-button-left TextInput-button-isRecording" 
                                    onClick={() => setIsRecording(false)}
                                    style={{width: '40%', height: '80%'}}>
                                <GiCancel />
                            </button>
                            <button className='TextInput-button TextInput-button-left TextInput-button-pauseRecording'
                                    style={{width: '40%', height: '80%'}}>
                                <FaPause />
                            </button>
                        </div>
                    ) : (
                        <button className="TextInput-button TextInput-button-left" onClick={() => setIsRecording(true)}>
                            <MdKeyboardVoice />
                        </button>
                    )
                }
                <button className="TextInput-button TextInput-button-right" onClick={() => handleSubmit(query, setQuery)}>
                    <FaArrowUp />
                </button>
            </div>

        </div>
    )
}

export default TextInput; 