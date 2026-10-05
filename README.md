# Group 4 — Social Media Sentiment Analysis

## Project Overview

This project implements a Big Data pipeline for analyzing social media data and performing sentiment prediction using distributed and real-time processing technologies.

The system uses historical social media data for machine learning and Kafka streaming for real-time data processing. Predictions and processed results are stored in MariaDB and displayed through a Django web dashboard.

## Project Architecture

```text
Large Social Media Dataset
          |
          v
        HDFS
          |
          v
   Kafka Producer
          |
          v
   Kafka Topic
   sentiment_data
          |
          v
 PySpark Structured Streaming
          |
          v
 Feature Engineering
          |
          v
 MLlib Sentiment Model
          |
          v
     Predictions
          |
          v
       MariaDB
          |
          v
   Django Dashboard
