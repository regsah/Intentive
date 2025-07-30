import React, { useState } from 'react';
import { MdKeyboardVoice, MdWidthFull } from "react-icons/md";
import './RecorderPage.css'
import TextInput from '../components/TextInput';

function RecorderPage() {
    const [isRecording, setIsRecording] = useState(false);
    const [isPaused, setIsPaused] = useState(false);
    
    return (
        <div className="RecorderPage-container">
            <div className={`RecorderPage-recording-symbol ${isRecording ? 'recording-active' : ''} ${isPaused ? 'recording-paused' : ''}`}>
                <MdKeyboardVoice style={{height:'80%', width:'80%'}}/>
            </div>
            <TextInput  isRecording={isRecording}
                        setIsRecording={setIsRecording} 
                        isPaused={isPaused}
                        setIsPaused={setIsPaused}/>
        </div>
    );
}

export default RecorderPage