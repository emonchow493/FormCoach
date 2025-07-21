import React, { useState, useEffect } from 'react';
import axios from 'axios';
import VideoCard from './VideoCard';

function VideoLibrary() {
  const [videos, setVideos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchVideos();
  }, []);

  const fetchVideos = async () => {
    try {
      setLoading(true);
      const response = await axios.get('/api/videos/');
      if (response.data.success) {
        setVideos(response.data.videos);
      } else {
        setError('Failed to fetch videos');
      }
    } catch (err) {
      setError('Error loading videos: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="loading">Loading exercise videos...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div>
      <h1>Exercise Video Library</h1>
      <p>Browse our collection of proper form exercise videos to learn correct techniques.</p>
      
      {videos.length === 0 ? (
        <div className="card">
          <p>No videos available. Please check back later.</p>
        </div>
      ) : (
        <div className="video-grid">
          {videos.map(video => (
            <VideoCard key={video.id} video={video} />
          ))}
        </div>
      )}
    </div>
  );
}

export default VideoLibrary;
