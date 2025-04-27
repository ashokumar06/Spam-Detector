import streamlit as st
import pickle
import string
import re
import spacy
from nltk.stem import PorterStemmer

# Check and load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import spacy.cli
    pass
    # spacy.cli.download("en_core_web_sm")
    # nlp = spacy.load("en_core_web_sm")

# Initialize stemmer and stopwords
stemmer = PorterStemmer()
stopwords_set = nlp.Defaults.stop_words  # spaCy's default stopwords

# Load pre-trained TfidfVectorizer and model
try:
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('mnb_model.pkl', 'rb'))
except FileNotFoundError as e:
    st.error("Required model files not found. Please ensure 'vectorizer.pkl' and 'mnb_model.pkl' are available.")
    st.stop()

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

# Input text field
input_sms = st.text_input("Enter your text")

# Prediction logic
if st.button("Predict"):
    if input_sms.strip():
        transformed_sms = transform_text(input_sms)
        try:
            vector_input = tfidf.transform([transformed_sms])
            result = model.predict(vector_input)[0]

            # Display the result
            if result == 0:
                st.header("The message is classified as Not Spam.")
            else:
                st.header("The message is classified as Spam.")
        except Exception as e:
            st.error("An error occurred during prediction: " + str(e))
    else:
        st.warning("Please enter some text to classify.")


st.markdown(
    """
    <style>
    .button-container {
        display: flex;
        justify-content: center;
        position: fixed;
        bottom: 20px;
        width: 100%;
    }
    .button-container a {
        font-size: 18px;
        padding: 10px 20px;
        background-color: #4CAF50;
        color: white;
        text-align: center;
        border-radius: 5px;
        text-decoration: none;
    }
    .button-container a:hover {
        background-color: #45a049;
    }
    </style>
    <div class="button-container">
        <a href="https://ashokumar.in" target="_blank">About Me</a>
    </div>
    """,
    unsafe_allow_html=True,
)
