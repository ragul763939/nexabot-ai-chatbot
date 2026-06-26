import json
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from nlp.text_cleaning import tokenize, stem, bag_of_words

with open('dataset/intents.json') as f:
    data = json.load(f)

all_words = []
tags = []
xy = []

for intent in data['intents']:
    tag = intent['tag']
    if tag not in tags:
        tags.append(tag)
    for pattern in intent['patterns']:
        words = tokenize(pattern)
        all_words.extend(words)
        xy.append((words, tag))

ignore = ['?', '!', '.', ',', "'s", "'m"]
all_words = sorted(set([stem(w) for w in all_words if w not in ignore]))
tags = sorted(tags)

X_train = []
y_train = []

for (pattern_words, tag) in xy:
    bag = bag_of_words(pattern_words, all_words)
    X_train.append(bag)
    y_train.append(tags.index(tag))

X_train = np.array(X_train)
y_train = np.array(y_train)

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

pickle.dump(model,     open('model/chatbot_model.pkl', 'wb'))
pickle.dump(all_words, open('model/all_words.pkl',     'wb'))
pickle.dump(tags,      open('model/tags.pkl',          'wb'))

print("Training complete!")
print(f"Vocabulary size : {len(all_words)} unique words")
print(f"Total intents   : {len(tags)}")
print(f"Training samples: {len(X_train)}")
print(f"Tags learned    : {tags}")
