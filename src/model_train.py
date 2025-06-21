# Import necessary libraries
import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
import os
import pickle

# Optional: turn off TensorFlow's oneDNN optimization warning
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

# Load intents file (make sure it's correctly named as 'intent.json' in your folder)
with open('intent.json') as file:
    data = json.load(file)

# Initialize variables for training
training_sentences = []
training_labels = []
labels = []
responses = []

# Extract sentences and labels from the JSON
for intent in data['intents']:
    for pattern in intent['patterns']:
        training_sentences.append(pattern)
        training_labels.append(intent['tag'])
    responses.append(intent['responses'])
    
    if intent['tag'] not in labels:
        labels.append(intent['tag'])

# Print number of unique intent classes
number_of_classes = len(labels)
print("Number of classes:", number_of_classes)

# Encode the labels (convert string labels to numbers)
label_encoder = LabelEncoder()
training_labels = label_encoder.fit_transform(training_labels)

# Define Tokenizer parameters
vocab_size = 1000
max_len = 20
oov_token = '<OOV>'
embedding_dim = 16

# Tokenize the sentences (convert words to numbers)
tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token)
tokenizer.fit_on_texts(training_sentences)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(training_sentences)
padded_sequences = pad_sequences(sequences, truncating='post', maxlen=max_len)

# Build the model
model = Sequential()
model.add(Embedding(vocab_size, embedding_dim, input_length=max_len))  # Embedding layer
model.add(GlobalAveragePooling1D())                                    # Reduce sequence to vector
model.add(Dense(16, activation='relu'))                                # Hidden layer 1
model.add(Dense(16, activation='relu'))                                # Hidden layer 2
model.add(Dense(number_of_classes, activation='softmax'))              # Output layer

# Compile the model
model.compile(
    loss='sparse_categorical_crossentropy',  # Fixed typo here
    optimizer='adam',
    metrics=['accuracy']                     # Fixed typo here
)

# Print model summary
model.summary()

history = model.fit(padded_sequences, np.array(training_labels), epochs = 1000)
model.save('chat_model.h5')

with open("tokenizer.pkl","wb") as f:
    pickle.dump(tokenizer, f, protocol=pickle.HIGHEST_PROTOCOL)

with open("label_encoder.pkl","wb") as encoder_file:
    pickle.dump(label_encoder, encoder_file, protocol=pickle.HIGHEST_PROTOCOL)