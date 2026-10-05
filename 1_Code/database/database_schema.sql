-- Group 4 Social Media Sentiment Analysis
-- Database Schema

CREATE DATABASE IF NOT EXISTS sentiment_analysis;

USE sentiment_analysis;

CREATE TABLE IF NOT EXISTS sentiment_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    original_text TEXT,
    sentiment DOUBLE,
    sentiment_label VARCHAR(20),
    prediction VARCHAR(20),
    primary_theme VARCHAR(100),
    main_emotion VARCHAR(100),
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);