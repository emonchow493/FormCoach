import os
import requests
import json
from typing import Dict, Any

class ChatAssistant:
    """Handles AI chat functionality"""
    
    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.openai_base_url = "https://api.openai.com/v1"
    
    def get_response(self, message: str) -> str:
        """Get AI response to user message"""
        if not self.openai_api_key:
            return self._get_dummy_response(message)
        
        try:
            headers = {
                "Authorization": f"Bearer {self.openai_api_key}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {
                        "role": "system",
                        "content": """You are FormCoach, an AI fitness assistant that helps users with exercise form and technique. 
                        You provide helpful, accurate, and safe fitness advice. Always encourage proper form and safety first.
                        Keep responses concise but informative."""
                    },
                    {
                        "role": "user",
                        "content": message
                    }
                ],
                "max_tokens": 300
            }
            
            response = requests.post(
                f"{self.openai_base_url}/chat/completions",
                headers=headers,
                json=payload
            )
            
            if response.status_code == 200:
                result = response.json()
                return result['choices'][0]['message']['content']
            else:
                print(f"OpenAI API error: {response.status_code}")
                return self._get_dummy_response(message)
                
        except Exception as e:
            print(f"Error getting chat response: {e}")
            return self._get_dummy_response(message)
    
    def _get_dummy_response(self, message: str) -> str:
        """Return dummy response for testing"""
        message_lower = message.lower()
        
        if 'squat' in message_lower:
            return "For proper squat form: Keep your feet shoulder-width apart, chest up, and lower your body as if sitting back into a chair. Make sure your knees don't go past your toes."
        elif 'deadlift' in message_lower:
            return "For deadlift form: Keep the bar close to your body, maintain a neutral spine, and drive through your heels. Don't round your back!"
        elif 'push-up' in message_lower or 'pushup' in message_lower:
            return "For push-up form: Keep your body in a straight line from head to heels, lower your chest to the ground, and push back up with control."
        elif 'form' in message_lower:
            return "Good form is crucial for preventing injuries and maximizing results. Always prioritize proper technique over lifting heavier weights."
        elif 'injury' in message_lower or 'pain' in message_lower:
            return "If you're experiencing pain during exercise, stop immediately and consult with a healthcare professional. It's better to be safe than sorry."
        else:
            return "I'm here to help with your fitness questions! Ask me about exercise form, technique, or any fitness-related topics."
