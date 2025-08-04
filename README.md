# Intentive

**Intentive** is a full-stack GenAI interface that enables users to send queries via voice or text. It features a React frontend, a FastAPI backend, speech-to-text processing, NLP-based intent and emotion classification, and a monitoring dashboard.

---

## Project Structure
```
intentive/
|
| - apps/
|   | - backend/    # FastAPI backend
|   | - webapp/     # React frontend
| - ffmpeg/         # FFmpeg
| - local_storage/  # Temporary storage for audio files and logs
```

---

## Installation & Setup

### 1. Clone the Repository
```
bash
git clone https://github.com/your-username/intentive.git
cd intentive
```

### 2. Install FFmpeg
Intentive requires FFmpeg to process voice input. Download from the link below and add it to the designated folder
Download: https://ffmpeg.org/download.html

### 3. Run the backend
```
cd apps/backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 4. Run the frontend
```
cd apps/webapp
npm install
npm run dev
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author
Developed by regsah

