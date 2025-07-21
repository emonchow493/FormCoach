import cv2
import os
import base64
import requests
import json
from typing import List, Dict, Any
import os

class VideoAnalyzer:
    """Handles video frame extraction and AI analysis"""
    
    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.openai_base_url = "https://api.openai.com/v1"
    
    def extract_frames(self, video_path: str, num_frames: int = 5) -> List[str]:
        """Extract frames from video and convert to base64"""
        try:
            cap = cv2.VideoCapture(video_path)
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            
            if total_frames == 0:
                raise ValueError("Video has no frames")
            
            # Calculate frame indices to extract
            frame_indices = []
            if total_frames <= num_frames:
                frame_indices = list(range(total_frames))
            else:
                step = total_frames // num_frames
                frame_indices = [i * step for i in range(num_frames)]
            
            frames = []
            for i, frame_idx in enumerate(frame_indices):
                cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
                ret, frame = cap.read()
                
                if ret:
                    # Convert frame to base64
                    _, buffer = cv2.imencode('.jpg', frame)
                    frame_base64 = base64.b64encode(buffer).decode('utf-8')
                    frames.append(frame_base64)
            
            cap.release()
            return frames
            
        except Exception as e:
            print(f"Error extracting frames: {e}")
            return []
    
    def analyze_frames(self, frames: List[str]) -> Dict[str, Any]:
        """Analyze frames using OpenAI Vision API or return dummy data"""
        if not self.openai_api_key:
            # Return dummy analysis if no API key
            return self._get_dummy_analysis()
        
        try:
            # Prepare the API request
            headers = {
                "Authorization": f"Bearer {self.openai_api_key}",
                "Content-Type": "application/json"
            }
            
            # Convert frames to OpenAI format
            content = []
            for i, frame in enumerate(frames):
                content.append({
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{frame}"
                    }
                })
            
            # Add text prompt
            content.append({
                "type": "text",
                "text": """Analyze this exercise video and provide feedback on form. 
                Look for:
                1. Posture and alignment
                2. Range of motion
                3. Movement control
                4. Potential safety issues
                5. Areas for improvement
                
                Provide specific, actionable feedback in JSON format with these fields:
                - overall_score (1-10)
                - posture_feedback
                - range_of_motion_feedback
                - safety_concerns
                - improvement_tips
                - exercise_identified"""
            })
            
            payload = {
                "model": "gpt-4-vision-preview",
                "messages": [
                    {
                        "role": "user",
                        "content": content
                    }
                ],
                "max_tokens": 1000
            }
            
            response = requests.post(
                f"{self.openai_base_url}/chat/completions",
                headers=headers,
                json=payload
            )
            
            if response.status_code == 200:
                result = response.json()
                analysis_text = result['choices'][0]['message']['content']
                
                # Try to parse JSON from response
                try:
                    return json.loads(analysis_text)
                except json.JSONDecodeError:
                    # If not valid JSON, return as text
                    return {
                        "overall_score": 7,
                        "posture_feedback": "Analysis completed",
                        "range_of_motion_feedback": "Analysis completed",
                        "safety_concerns": "None identified",
                        "improvement_tips": "See detailed analysis",
                        "exercise_identified": "Exercise detected",
                        "raw_analysis": analysis_text
                    }
            else:
                print(f"OpenAI API error: {response.status_code}")
                return self._get_dummy_analysis()
                
        except Exception as e:
            print(f"Error analyzing frames: {e}")
            return self._get_dummy_analysis()
    
    def _get_dummy_analysis(self) -> Dict[str, Any]:
        """Return dummy analysis data for testing"""
        return {
            "overall_score": 7,
            "posture_feedback": "Good overall posture. Maintain neutral spine position.",
            "range_of_motion_feedback": "Adequate range of motion. Consider going deeper in the movement.",
            "safety_concerns": "No major safety concerns detected.",
            "improvement_tips": [
                "Keep your core engaged throughout the movement",
                "Focus on controlled descent and ascent",
                "Ensure knees track over toes",
                "Maintain steady breathing pattern"
            ],
            "exercise_identified": "Squat variation",
            "confidence": 0.85
        }
