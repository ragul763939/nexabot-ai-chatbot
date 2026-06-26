# NexaBot - AI College Assistant Chatbot

An AI-powered chatbot built with Python NLP, Machine Learning, and Flask.

## Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- NLP: NLTK (tokenization, stemming, bag-of-words)
- ML: scikit-learn (Random Forest Classifier)
- Dataset: 41 intents, 278 patterns

## How to Run

1. Install dependencies:
   pip3 install -r requirements.txt

2. Train the model (only needed once):
   python3 model/train_model.py

3. Start the server:
   python3 backend/app.py

4. Open your browser at:
   http://127.0.0.1:8000

## Project Structure
- dataset/intents.json   - Training data (intents, patterns, responses)
- nlp/text_cleaning.py    - NLP preprocessing functions
- model/train_model.py    - ML model training script
- model/*.pkl             - Saved trained model files
- backend/app.py          - Flask API server
- frontend/chatbot.html   - Chat user interface

## Features
- Intent recognition using NLP and Machine Learning
- Confidence scoring for each response
- Fallback handling for unknown queries
- Clean, modern chat interface
