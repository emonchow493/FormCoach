import os
import json
from flask import Blueprint, request, jsonify, current_app
from ..models.user_upload import UserUpload
from ..utils.video_analyzer import VideoAnalyzer
from .. import db

bp = Blueprint('analyze', __name__, url_prefix='/api/analyze')

@bp.route('/', methods=['POST'])
def analyze_video():
    """Analyze uploaded video using AI vision"""
    try:
        data = request.get_json()
        upload_id = data.get('upload_id')
        
        if not upload_id:
            return jsonify({
                'success': False,
                'error': 'Upload ID is required'
            }), 400
        
        # Get upload record
        upload_record = UserUpload.query.get(upload_id)
        if not upload_record:
            return jsonify({
                'success': False,
                'error': 'Upload record not found'
            }), 404
        
        # Check if file exists
        if not os.path.exists(upload_record.file_path):
            return jsonify({
                'success': False,
                'error': 'Video file not found'
            }), 404
        
        # Initialize video analyzer
        analyzer = VideoAnalyzer()
        
        # Extract frames and analyze
        frames = analyzer.extract_frames(upload_record.file_path, num_frames=5)
        analysis_result = analyzer.analyze_frames(frames)
        
        # Update upload record with analysis result
        upload_record.analysis_result = json.dumps(analysis_result)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'analysis': analysis_result,
            'upload_id': upload_id
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
