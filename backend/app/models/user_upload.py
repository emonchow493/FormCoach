from .. import db
from datetime import datetime

class UserUpload(db.Model):
    """Model for storing user uploaded videos"""
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    original_filename = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    file_size = db.Column(db.Integer, nullable=False)
    mime_type = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    analysis_result = db.Column(db.Text, nullable=True)  # JSON string of AI analysis
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        """Convert model to dictionary for JSON response"""
        return {
            'id': self.id,
            'filename': self.filename,
            'original_filename': self.original_filename,
            'file_size': self.file_size,
            'mime_type': self.mime_type,
            'analysis_result': self.analysis_result,
            'created_at': self.created_at.isoformat()
        }
    
    def __repr__(self):
        return f'<UserUpload {self.original_filename}>'
