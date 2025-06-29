import json
import pickle
from tensorflow.keras.models import load_model
import random
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

with open('intent.json') as file:
    data = json.load(file)
model = load_model('chat_model.h5')

with open("tokenizer.pkl","rb") as f:
    tokenizer = pickle.load(f)

with open("label_encoder.pkl","rb") as encoder_file:
   label_encoder = pickle.load(encoder_file)

while True:
    input_text = input("Enter Youe Command-> ")
    padded_sequences = pad_sequences(tokenizer.texts_to_sequences([input_text]), maxlen=20, truncating='post')
    result = model.predict(padded_sequences)
    tag = label_encoder.inverse_transform([np.argmax(result)])
    
    for i in data['intents']:
        if i['tag'] == tag:
            print(np.random.choice(i['responses'])) 