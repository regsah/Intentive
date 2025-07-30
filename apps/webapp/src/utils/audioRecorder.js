export default class AudioRecorder {
    constructor() {
        this.mediaRecorder = null;
        this.stream = null;
        this.chunks = [];
    }

    async init() {
        if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
            throw new Error('getUserMedia is not supported in this browser.');
        }

        this.stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        this.mediaRecorder = new MediaRecorder(this.stream);
    
        this.mediaRecorder.ondataavailable = (event) => {
            if (event.data.size > 0) {
                this.chunks.push(event.data);
            }
        };
    }

    start() {
        this.chunks = [];
        if (!this.mediaRecorder) {
            throw new Error('Recorder is not initialized. Call init() first.');
        }
        if (this.mediaRecorder.state === 'recording') {
            throw new Error('Recording already started');
        }


        this.mediaRecorder.start();
    }

    pause() {
        if (!this.mediaRecorder) throw new Error('Recorder not initialized');
        if (this.mediaRecorder.state !== 'recording') {
            throw new Error(`Cannot pause while state is '${this.mediaRecorder.state}'`);
        }
        this.mediaRecorder.pause();
    }

    resume() {
        if (!this.mediaRecorder) throw new Error('Recorder not initialized');
        if (this.mediaRecorder.state !== 'paused') {
            throw new Error(`Cannot resume while state is '${this.mediaRecorder.state}'`);
        }
        this.mediaRecorder.resume();
    }

    async stop() {
        if (!this.mediaRecorder) throw new Error('Recorder not initialized');
        if (this.mediaRecorder.state === 'inactive') {
            throw new Error('Recorder is already stopped');
        }

        return new Promise((resolve) => {
            this.mediaRecorder.onstop = () => {
                const blob = new Blob(this.chunks, { type: 'audio/webm' });
                this.cleanup();
                resolve(blob);
            };
            this.mediaRecorder.stop();
        });
    }

    abort() {
        if (this.mediaRecorder && this.mediaRecorder.state !== 'inactive') {
            this.mediaRecorder.stop();
        }
        this.cleanup();
        console.log('Recording aborted and data discarded.');
    }


    cleanup() {
        if (this.stream) {
            this.stream.getTracks().forEach(track => track.stop());
        }

        this.stream = null;

        if (this.mediaRecorder) {
            this.mediaRecorder.ondataavailable = null;
            this.mediaRecorder.onstop = null;
        }

        this.mediaRecorder = null;
        this.chunks = [];
    }
}
