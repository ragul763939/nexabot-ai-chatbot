import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
import pickle
import random
import numpy as np
from flask import Flask, request, jsonify, render_template
from nlp.text_cleaning import tokenize, bag_of_words, stem

app = Flask(__name__, template_folder='../frontend')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model     = pickle.load(open(os.path.join(BASE,'model/chatbot_model.pkl'), 'rb'))
all_words = pickle.load(open(os.path.join(BASE,'model/all_words.pkl'), 'rb'))
tags      = pickle.load(open(os.path.join(BASE,'model/tags.pkl'), 'rb'))

with open(os.path.join(BASE,'dataset/intents.json')) as f:
    intents = json.load(f)

def get_response(user_message):
    words    = tokenize(user_message)
    bag      = bag_of_words(words, all_words)
    probs    = model.predict_proba([bag])[0]
    max_prob = max(probs)
    if max_prob < 0.3:
        return "I am not sure I understood that. Can you rephrase?", "unknown", round(max_prob * 100)
    tag_idx  = list(probs).index(max_prob)
    tag      = tags[tag_idx]
    for intent in intents['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses']), tag, round(max_prob * 100)
    return "I could not find a response.", tag, 0

@app.route('/')
def home():
    return render_template('chatbot.html')

@app.route('/chat', methods=['POST'])
def chat():
    data     = request.get_json()
    message  = data.get('message', '')
    response, tag, confidence = get_response(message)
    return jsonify({
        'response':   response,
        'intent':     tag,
        'confidence': f'{confidence}%'
    })

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8000)); app.run(host='0.0.0.0', port=port)
