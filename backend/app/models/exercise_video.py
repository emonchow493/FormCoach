from .. import db
from datetime import datetime

class ExerciseVideo(db.Model):
    """Model for storing correct form exercise videos"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    video_url = db.Column(db.String(500), nullable=False)
    thumbnail_url = db.Column(db.String(500), nullable=True)
    category = db.Column(db.String(100), nullable=True)
    difficulty = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        """Convert model to dictionary for JSON response"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'video_url': self.video_url,
            'thumbnail_url': self.thumbnail_url,
            'category': self.category,
            'difficulty': self.difficulty,
            'created_at': self.created_at.isoformat()
        }
    
    def __repr__(self):
        return f'<ExerciseVideo {self.title}>'
