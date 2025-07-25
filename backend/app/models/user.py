from .. import db
from datetime import datetime

class User(db.Model):
    """User model for future authentication"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    uploads = db.relationship('UserUpload', backref='user', lazy=True)
    
    def __repr__(self):
        return f'<User {self.username}>'
