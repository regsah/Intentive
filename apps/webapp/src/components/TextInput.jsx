import React, { useState, useRef, useEffect } from 'react';

import { MdKeyboardVoice } from "react-icons/md";
import { FaArrowUp } from "react-icons/fa";
import { GiCancel } from "react-icons/gi";
import { FaPause } from "react-icons/fa6";
import { FaCaretRight } from "react-icons/fa";


import './styles/TextInput.css'

import AudioRecorder from '../utils/audioRecorder.js';

function TextInput({isRecording, setIsRecording, isPaused, setIsPaused}) {
    async function handleStart() {
        try {
            const recorder = recorderRef.current;
            if (!recorder.mediaRecorder || recorder.mediaRecorder.state === 'inactive') {
                await recorder.init();
            }

            recorder.start();
            setIsRecording(true);
            setIsPaused(false);
        } catch (error) {
            console.error("Failed to start recording:", error);
        }
    }

    function handlePause() {
        const recorder = recorderRef.current;
        if (!recorder.mediaRecorder) return;

        try {
            if(recorder.mediaRecorder.state === 'paused') {
                recorder.resume();
                setIsPaused(false);
            }
            else if(recorder.mediaRecorder.state === 'recording') {
                recorder.pause();
                setIsPaused(true);
            }
        } catch (error) {
            console.error(
                recorder.mediaRecorder.state === 'paused' 
                    ? "Failed to resume recording:" 
                    : "Failed to pause recording:", 
                error
            );
        }
    }

    function handleAbort() {
        const recorder = recorderRef.current;
        if (!recorder.mediaRecorder) return;

        try {
            recorder.abort();
            setIsRecording(false);
            setIsPaused(false);
        } catch (error) {
            console.error("Failed to abort recording:", error);
        }
    }

    async function handleSubmit() {
        const recorder = recorderRef.current;

        try {
            if (isRecording) {
                const audioBlob = await recorder.stop();
                setIsRecording(false);
                setIsPaused(false);

                const url = URL.createObjectURL(audioBlob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'recording.webm';
                document.body.appendChild(a);
                a.click();
                a.remove();
                URL.revokeObjectURL(url);
                
                setQuery('');
            } else {
                console.log('Text query:', query);
                setQuery('');
            }
        } catch (error) {
            console.error('Failed to submit recording or text:', error);
        }
    }


    const recorderRef = useRef(new AudioRecorder());
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
                                    style={{width: '40%', height: '80%'}}
                                    onClick={() => handleAbort()}>
                                <GiCancel />
                            </button>
                            <button className='TextInput-button TextInput-button-left TextInput-button-pauseRecording'
                                    style={{width: '40%', height: '80%'}}
                                    onClick={() => handlePause()}>
                                {isPaused ? <FaCaretRight /> : <FaPause />}
                            </button>
                        </div>
                    ) : (
                        <button className="TextInput-button TextInput-button-left" 
                                onClick={() => handleStart()}>
                            <MdKeyboardVoice />
                        </button>
                    )
                }
                <button className="TextInput-button TextInput-button-right" 
                        onClick={() => handleSubmit()}>
                    <FaArrowUp />
                </button>
            </div>

        </div>
    )
}

export default TextInput; 