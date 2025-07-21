import React, { useState } from 'react';
import axios from 'axios';

function UploadForm() {
  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [uploadId, setUploadId] = useState(null);
  const [analyzing, setAnalyzing] = useState(false);
  const [analysis, setAnalysis] = useState(null);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      // Check file type
      const allowedTypes = ['video/mp4', 'video/avi', 'video/mov', 'video/mkv', 'video/webm'];
      if (!allowedTypes.includes(selectedFile.type)) {
        setError('Please select a valid video file (MP4, AVI, MOV, MKV, or WEBM)');
        return;
      }
      
      // Check file size (16MB limit)
      if (selectedFile.size > 16 * 1024 * 1024) {
        setError('File size must be less than 16MB');
        return;
      }
      
      setFile(selectedFile);
      setError(null);
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setError('Please select a video file');
      return;
    }

    try {
      setUploading(true);
      setError(null);
      
      const formData = new FormData();
      formData.append('video', file);
      
      const response = await axios.post('/api/upload/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      
      if (response.data.success) {
        setUploadId(response.data.upload_id);
        setSuccess('Video uploaded successfully!');
        setFile(null);
        // Reset file input
        document.getElementById('video-file').value = '';
      } else {
        setError(response.data.error || 'Upload failed');
      }
    } catch (err) {
      setError('Upload failed: ' + err.message);
    } finally {
      setUploading(false);
    }
  };

  const handleAnalyze = async () => {
    if (!uploadId) {
      setError('Please upload a video first');
      return;
    }

    try {
      setAnalyzing(true);
      setError(null);
      
      const response = await axios.post('/api/analyze/', {
        upload_id: uploadId
      });
      
      if (response.data.success) {
        setAnalysis(response.data.analysis);
        setSuccess('Analysis completed!');
      } else {
        setError(response.data.error || 'Analysis failed');
      }
    } catch (err) {
      setError('Analysis failed: ' + err.message);
    } finally {
      setAnalyzing(false);
    }
  };

  return (
    <div>
      <h1>Upload Your Workout Video</h1>
      <p>Upload a short video of your exercise to get AI-powered form feedback.</p>
      
      <div className="upload-form">
        {error && <div className="error">{error}</div>}
        {success && <div className="success">{success}</div>}
        
        <div className="form-group">
          <label htmlFor="video-file">Select Video File:</label>
          <input
            type="file"
            id="video-file"
            accept="video/*"
            onChange={handleFileChange}
            disabled={uploading}
          />
        </div>
        
        <button 
          className="btn btn-primary" 
          onClick={handleUpload}
          disabled={!file || uploading}
        >
          {uploading ? 'Uploading...' : 'Upload Video'}
        </button>
        
        {uploadId && (
          <div style={{ marginTop: '20px' }}>
            <button 
              className="btn btn-secondary" 
              onClick={handleAnalyze}
              disabled={analyzing}
            >
              {analyzing ? 'Analyzing...' : 'Analyze Form'}
            </button>
          </div>
        )}
        
        {analysis && (
          <div className="card" style={{ marginTop: '20px' }}>
            <h3>Form Analysis Results</h3>
            <div>
              <p><strong>Overall Score:</strong> {analysis.overall_score}/10</p>
              <p><strong>Posture Feedback:</strong> {analysis.posture_feedback}</p>
              <p><strong>Range of Motion:</strong> {analysis.range_of_motion_feedback}</p>
              <p><strong>Safety Concerns:</strong> {analysis.safety_concerns}</p>
              <p><strong>Exercise Identified:</strong> {analysis.exercise_identified}</p>
              
              {analysis.improvement_tips && (
                <div>
                  <strong>Improvement Tips:</strong>
                  <ul>
                    {Array.isArray(analysis.improvement_tips) 
                      ? analysis.improvement_tips.map((tip, index) => (
                          <li key={index}>{tip}</li>
                        ))
                      : <li>{analysis.improvement_tips}</li>
                    }
                  </ul>
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default UploadForm;
