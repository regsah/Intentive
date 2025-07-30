import React, { useState } from 'react';
import { MdKeyboardVoice, MdWidthFull } from "react-icons/md";
import './RecorderPage.css'
import TextInput from '../components/TextInput';

function RecorderPage() {
    const [isRecording, setIsRecording] = useState(false);
    
    return (
        <div className="RecorderPage-container">
            <div className={`RecorderPage-recording-symbol ${isRecording ? 'recording-active' : ''}`}>
                <MdKeyboardVoice style={{height:'80%', width:'80%'}}/>
            </div>
            <TextInput isRecording={isRecording} setIsRecording={setIsRecording} />
        </div>
    );
}

export default RecorderPage