import streamlit as st
import pickle
import string
import re
import spacy
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

# Load spaCy model
nlp = spacy.load("en_core_web_sm")
stemmer = PorterStemmer()
stopwords_set = nlp.Defaults.stop_words  # spaCy's default stopwords

# Load pre-trained TfidfVectorizer and model
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('mnb_model.pkl', 'rb'))

# Text preprocessing function
def transform_text(text):
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
    text = re.sub(r'\d+', '', text)  # Remove numbers
    tokens = [token.text for token in nlp(text)]  # Tokenize text using spaCy
    tokens = [token for token in tokens if token.isalpha()]  # Keep only alphabetic tokens
    tokens = [token for token in tokens if token not in stopwords_set]  # Remove stopwords
    stemmed_tokens = [stemmer.stem(token) for token in tokens]  # Stem tokens
    return " ".join(stemmed_tokens)

# Streamlit app
st.title("Spam Classifier")

input_sms = st.text_input("Enter your text")

if st.button("Predict"):
    # Preprocess the input
    transformed_sms = transform_text(input_sms)
    try:
        vector_input = tfidf.transform([transformed_sms])
    except ValueError as e:
        st.error("An error occurred during vectorization: " + str(e))
        st.stop()
    result = model.predict(vector_input)[0]

    # Display the result
    if result == 0:
        st.header("The message is classified as Not Spam.")
    else:
        st.header("The message is classified as Spam.")
