from app import create_app, db
from app.models.exercise_video import ExerciseVideo

def seed_exercise_videos():
    """Seed the database with sample exercise videos"""
    app = create_app()
    
    with app.app_context():
        # Check if videos already exist
        if ExerciseVideo.query.count() > 0:
            print("Exercise videos already seeded")
            return
        
        # Sample exercise videos
        videos = [
            {
                'title': 'Perfect Squat Form',
                'description': 'Learn the proper technique for performing squats with correct form and posture.',
                'video_url': 'https://www.youtube.com/embed/example1',
                'thumbnail_url': 'https://via.placeholder.com/300x200/4CAF50/FFFFFF?text=Squat+Form',
                'category': 'Lower Body',
                'difficulty': 'Beginner'
            },
            {
                'title': 'Deadlift Mastery',
                'description': 'Master the deadlift with proper form to build strength and prevent injury.',
                'video_url': 'https://www.youtube.com/embed/example2',
                'thumbnail_url': 'https://via.placeholder.com/300x200/2196F3/FFFFFF?text=Deadlift+Form',
                'category': 'Lower Body',
                'difficulty': 'Intermediate'
            },
            {
                'title': 'Push-Up Progression',
                'description': 'From beginner to advanced push-up variations with perfect form.',
                'video_url': 'https://www.youtube.com/embed/example3',
                'thumbnail_url': 'https://via.placeholder.com/300x200/FF9800/FFFFFF?text=Push-Up+Form',
                'category': 'Upper Body',
                'difficulty': 'Beginner'
            },
            {
                'title': 'Plank Variations',
                'description': 'Core strengthening exercises with proper plank form and variations.',
                'video_url': 'https://www.youtube.com/embed/example4',
                'thumbnail_url': 'https://via.placeholder.com/300x200/9C27B0/FFFFFF?text=Plank+Form',
                'category': 'Core',
                'difficulty': 'Beginner'
            },
            {
                'title': 'Lunge Technique',
                'description': 'Perfect your lunge form for better balance and leg strength.',
                'video_url': 'https://www.youtube.com/embed/example5',
                'thumbnail_url': 'https://via.placeholder.com/300x200/F44336/FFFFFF?text=Lunge+Form',
                'category': 'Lower Body',
                'difficulty': 'Beginner'
            }
        ]
        
        for video_data in videos:
            video = ExerciseVideo(**video_data)
            db.session.add(video)
        
        db.session.commit()
        print(f"Seeded {len(videos)} exercise videos")

if __name__ == '__main__':
    seed_exercise_videos()
