import string
import re
import spacy
from nltk.stem import PorterStemmer
import streamlit as st

class TextProcessor:
    """Text preprocessing class for spam classification"""
    
    def __init__(self):
        self.stemmer = PorterStemmer()
        self.nlp = self._load_spacy_model()
        self.stopwords_set = self.nlp.Defaults.stop_words
    
    def _load_spacy_model(self):
        """Load spaCy model with error handling"""
        try:
            return spacy.load("en_core_web_sm")
        except OSError:
            st.error("spaCy model 'en_core_web_sm' not found. Please install it using: python -m spacy download en_core_web_sm")
            st.stop()
    
    def transform_text(self, text):
        """
        Transform text for spam classification
        
        Args:
            text (str): Input text to process
            
        Returns:
            str: Processed text ready for vectorization
        """
        if not text or not isinstance(text, str):
            return ""
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove punctuation
        text = text.translate(str.maketrans("", "", string.punctuation))
        
        # Remove numbers
        text = re.sub(r'\d+', '', text)
        
        # Tokenize using spaCy
        tokens = [token.text for token in self.nlp(text)]
        
        # Keep only alphabetic tokens
        tokens = [token for token in tokens if token.isalpha()]
        
        # Remove stopwords
        tokens = [token for token in tokens if token not in self.stopwords_set]
        
        # Stem tokens
        stemmed_tokens = [self.stemmer.stem(token) for token in tokens]
        
        return " ".join(stemmed_tokens)
    
    def get_text_stats(self, text):
        """
        Get statistics about the input text
        
        Args:
            text (str): Input text
            
        Returns:
            dict: Text statistics
        """
        if not text:
            return {}
        
        processed_text = self.transform_text(text)
        doc = self.nlp(text)
        
        return {
            "original_length": len(text),
            "word_count": len(text.split()),
            "processed_length": len(processed_text),
            "processed_word_count": len(processed_text.split()),
            "sentence_count": len(list(doc.sents)),
            "char_count_no_spaces": len(text.replace(" ", "")),
            "uppercase_count": sum(1 for c in text if c.isupper()),
            "punctuation_count": sum(1 for c in text if c in string.punctuation),
            "number_count": len(re.findall(r'\d+', text))
        }