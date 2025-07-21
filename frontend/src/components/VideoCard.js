import React from 'react';

function VideoCard({ video }) {
  return (
    <div className="video-card">
      <img 
        src={video.thumbnail_url} 
        alt={video.title}
        className="video-thumbnail"
        onError={(e) => {
          e.target.src = 'https://via.placeholder.com/300x200/cccccc/666666?text=Video+Thumbnail';
        }}
      />
      <div className="video-content">
        <h3 className="video-title">{video.title}</h3>
        <p className="video-description">{video.description}</p>
        <div className="video-meta">
          <span className="video-category">{video.category}</span>
          <span className="video-difficulty">{video.difficulty}</span>
        </div>
      </div>
    </div>
  );
}

export default VideoCard;
