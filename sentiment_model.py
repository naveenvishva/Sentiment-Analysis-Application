import json
import nltk
from nltk.tokenize import word_tokenize
from tensorflow import keras
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Download the required NLTK resource
nltk.download('punkt')

# Load the saved model
model_filename = 'sentiment_model.h5'
model = keras.models.load_model(model_filename)

# Load the tokenizer configuration from your JSON data
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Extract the "text" values from the JSON data
texts = [item['text'] for item in data]

# Configure the tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)

# Set the maximum sequence length based on your data
max_sequence_length = 9  # You should adjust this based on your data

def predict_sentiment(input_text):
    tokenized_text = tokenizer.texts_to_sequences([input_text])[0]
    padded_text = pad_sequences([tokenized_text], maxlen=max_sequence_length)
    prediction = model.predict(padded_text)
    sentiment = "Positive" if prediction > 0.5 else "Negative"
    return sentiment
