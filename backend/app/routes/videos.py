from flask import Blueprint, jsonify
from ..models.exercise_video import ExerciseVideo

bp = Blueprint('videos', __name__, url_prefix='/api/videos')

@bp.route('/', methods=['GET'])
def get_videos():
    """Get all exercise videos"""
    try:
        videos = ExerciseVideo.query.all()
        return jsonify({
            'success': True,
            'videos': [video.to_dict() for video in videos]
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@bp.route('/<int:video_id>', methods=['GET'])
def get_video(video_id):
    """Get a specific exercise video"""
    try:
        video = ExerciseVideo.query.get_or_404(video_id)
        return jsonify({
            'success': True,
            'video': video.to_dict()
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
