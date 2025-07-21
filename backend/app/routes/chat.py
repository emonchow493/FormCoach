from flask import Blueprint, request, jsonify
from ..utils.chat_assistant import ChatAssistant

bp = Blueprint('chat', __name__, url_prefix='/api/chat')

@bp.route('/', methods=['POST'])
def chat():
    """Handle AI chat questions"""
    try:
        data = request.get_json()
        message = data.get('message')
        
        if not message:
            return jsonify({
                'success': False,
                'error': 'Message is required'
            }), 400
        
        # Initialize chat assistant
        assistant = ChatAssistant()
        
        # Get AI response
        response = assistant.get_response(message)
        
        return jsonify({
            'success': True,
            'response': response,
            'message': message
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
