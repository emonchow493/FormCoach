import pytest
from backend.app import create_app, db
from backend.app.models.exercise_video import ExerciseVideo

@pytest.fixture
def app():
    """Create application for testing"""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    """Create test client"""
    return app.test_client()

def test_get_videos(client):
    """Test getting all videos"""
    response = client.get('/api/videos/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert 'videos' in data

def test_upload_video_no_file(client):
    """Test upload without file"""
    response = client.post('/api/upload/')
    assert response.status_code == 400
    data = response.get_json()
    assert data['success'] is False
    assert 'No video file provided' in data['error']

def test_chat_no_message(client):
    """Test chat without message"""
    response = client.post('/api/chat/', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data['success'] is False
    assert 'Message is required' in data['error']

def test_chat_with_message(client):
    """Test chat with message"""
    response = client.post('/api/chat/', json={'message': 'How to do squats?'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert 'response' in data
