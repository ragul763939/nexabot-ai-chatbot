# 🤖 NexaBot — AI College Assistant Chatbot

An AI-powered chatbot that answers college students' questions about exams, placements, internships, stress, and general college life. Built from scratch using **Natural Language Processing (NLP)** and **Machine Learning**, with a Python Flask backend and a clean, responsive chat interface.

---

## ✨ Features

- **Intent recognition** — understands what the user is asking using a trained ML model
- **Confidence scoring** — every reply shows how confident the model is
- **Fallback handling** — gracefully responds when it doesn't understand a question
- **NLP pipeline** — tokenization, stemming, and bag-of-words preprocessing
- **Clean chat UI** — responsive interface with typing animation and suggestion chips
- **41 intents, 278 patterns** — covers a wide range of college-related topics

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| NLP | NLTK (tokenization, stemming, bag-of-words) |
| Machine Learning | scikit-learn (Random Forest Classifier) |
| Dataset | JSON |
| Tools | Git, GitHub, VS Code |

---

## 📂 Project Structure

```
AI_Chatbot/
├── dataset/
│   └── intents.json          # Training data (intents, patterns, responses)
├── nlp/
│   ├── __init__.py           # Marks nlp as a Python package
│   └── text_cleaning.py      # Tokenize, stem, bag-of-words functions
├── model/
│   ├── train_model.py        # Trains and saves the ML model
│   ├── chatbot_model.pkl     # Saved trained model
│   ├── all_words.pkl         # Saved vocabulary
│   └── tags.pkl              # Saved intent tags
├── backend/
│   └── app.py                # Flask server and API routes
├── frontend/
│   └── chatbot.html          # Chat user interface
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## ⚙️ How It Works

A single user message flows through the system in six steps:

1. The user types a message in the chat interface (`chatbot.html`).
2. JavaScript sends the message to the Flask backend (`app.py`) at the `/chat` route.
3. The NLP pipeline (`text_cleaning.py`) tokenizes and stems the text.
4. The words are converted into a bag-of-words numeric array.
5. The trained Random Forest model predicts the intent and a confidence score.
6. Flask returns a matching response, displayed with its intent and confidence.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed

### 1. Clone the repository
```bash
git clone https://github.com/ragul763939/nexabot-ai-chatbot.git
cd nexabot-ai-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the model (only needed once)
```bash
python model/train_model.py
```

### 4. Start the server
```bash
python backend/app.py
```

### 5. Open in your browser
```
http://127.0.0.1:8000
```

---

## 💬 Example Conversations

| You say | NexaBot detects | Example reply |
|---|---|---|
| "Hello" | greeting | "Hello! How can I help you today?" |
| "How to prepare for placements?" | placement_preparation | Tips on DSA, projects, and mock interviews |
| "I am stressed about exams" | stress | Supportive, encouraging response |
| "asdkjh" (gibberish) | unknown | "I'm not sure I understood that. Can you rephrase?" |

---

## 🔮 Future Improvements

- Add conversation memory for multi-turn context
- Expand the dataset with more intents and patterns
- Integrate a Large Language Model (LLM) API for open-ended questions
- Move the dataset to a database
- Deploy online with a production WSGI server

---

## 📚 What I Learned

Building this project end-to-end, I learned:
- Natural Language Processing preprocessing with NLTK
- Training, evaluating, and saving a machine learning model
- Building a REST API with Flask
- Connecting a frontend to a backend
- Debugging real deployment issues
- Version control with Git and GitHub

---

## 📄 License

This project was built for educational purposes.

---

*Built with Python, NLP, and Machine Learning.*