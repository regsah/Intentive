import React, { useState, useRef, useEffect } from 'react';

import { MdKeyboardVoice } from "react-icons/md";
import { FaArrowUp } from "react-icons/fa";
import { GiCancel } from "react-icons/gi";
import { FaPause } from "react-icons/fa6";
import { FaCaretRight } from "react-icons/fa";

import './styles/TextInput.css'

import AudioRecorder from '../utils/audioRecorder.js';

import axios from 'axios';
import { v4 as uuidv4 } from 'uuid'; 

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
            const uniqueId = uuidv4();

            if (isRecording) {
                const audioBlob = await recorder.stop();
                setIsRecording(false);
                setIsPaused(false);

                const formData = new FormData();
                formData.append('id', uniqueId);
                formData.append('audio', audioBlob, `recording_${uniqueId}.webm`);

                const response = await axios.post('http://localhost:8000/api/submit_audio', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                });

                console.log('Audio upload response:', response.data);
            } else {
                const response = await axios.post('http://localhost:8000/api/submit_text', { id: uniqueId, text: query });
                console.log('Text submission response:', response.data);
            }
            setQuery('');
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