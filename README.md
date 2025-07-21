# FormCoach - AI-Powered Exercise Form Analysis

FormCoach is a full-stack web application that helps users learn and maintain proper exercise form through AI-powered video analysis and interactive chat assistance.

## 🎯 Features

- **Video Library**: Browse a collection of correct form exercise videos
- **AI Form Analysis**: Upload workout videos for AI-powered form feedback
- **Interactive Chat**: Ask questions about exercise technique and get AI responses
- **Modern UI**: Clean, responsive React frontend
- **RESTful API**: Flask backend with comprehensive endpoints

## 🏗️ Architecture

### Frontend (React)
- **Framework**: React 18 with Create React App
- **Routing**: React Router for navigation
- **HTTP Client**: Axios for API communication
- **Styling**: CSS modules with modern design

### Backend (Flask)
- **Framework**: Flask with SQLAlchemy ORM
- **Database**: PostgreSQL (with SQLite fallback for development)
- **AI Integration**: OpenAI Vision API for video analysis
- **File Handling**: Secure video upload and processing
- **CORS**: Cross-origin resource sharing enabled

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+ (for frontend development)
- PostgreSQL (optional, SQLite works for development)

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/emonchow493/FormCoach.git
   cd FormCoach
   ```

2. **Set up Python environment**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp ../.env.example .env
   # Edit .env with your configuration
   ```

4. **Initialize database and seed data**
   ```bash
   python seed_data.py
   ```

5. **Run the backend server**
   ```bash
   python run.py
   ```
   The backend will be available at `http://localhost:5000`

### Frontend Setup

1. **Install dependencies**
   ```bash
   cd frontend
   npm install
   ```

2. **Start the development server**
   ```bash
   npm start
   ```
   The frontend will be available at `http://localhost:3000`

## 📁 Project Structure

```
FormCoach/
├── backend/
│   ├── app/
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── exercise_video.py
│   │   │   └── user_upload.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── videos.py
│   │   │   ├── upload.py
│   │   │   ├── analyze.py
│   │   │   └── chat.py
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── video_analyzer.py
│   │   │   └── chat_assistant.py
│   │   └── __init__.py
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_routes.py
│   ├── requirements.txt
│   ├── run.py
│   └── seed_data.py
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.js
│   │   │   ├── VideoLibrary.js
│   │   │   ├── VideoCard.js
│   │   │   ├── UploadForm.js
│   │   │   └── Chat.js
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   └── index.css
│   └── package.json
├── Dockerfile
├── .env.example
└── README.md
```

## 🔧 API Endpoints

### Videos
- `GET /api/videos/` - Get all exercise videos
- `GET /api/videos/<id>` - Get specific video

### Upload
- `POST /api/upload/` - Upload video file

### Analysis
- `POST /api/analyze/` - Analyze uploaded video

### Chat
- `POST /api/chat/` - Send message to AI assistant

## 🧪 Testing

Run backend tests:
```bash
cd backend
pytest
```

## 🐳 Docker Deployment

Build and run with Docker:
```bash
docker build -t formcoach .
docker run -p 5000:5000 formcoach
```

## 🔑 Environment Variables

Create a `.env` file in the backend directory:

```env
# Database
DATABASE_URL=postgresql://username:password@localhost:5432/formcoach

# Flask
SECRET_KEY=your-secret-key-here
FLASK_ENV=development

# OpenAI
OPENAI_API_KEY=your-openai-api-key-here

# Upload
MAX_CONTENT_LENGTH=16777216
UPLOAD_FOLDER=uploads
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 🆘 Support

For support, email support@formcoach.com or create an issue in the repository.
