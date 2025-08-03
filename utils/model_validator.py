import pickle
import streamlit as st
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

class ModelValidator:
    """Utility class to validate and load models safely"""
    
    @staticmethod
    def find_model_files():
        """Find model files in various possible locations"""
        possible_locations = [
            # Root directory (your original location)
            ('vectorizer.pkl', 'mnb_model.pkl'),
            # Models directory
            ('models/vectorizer.pkl', 'models/mnb_model.pkl'),
            # Other common locations
            ('model/vectorizer.pkl', 'model/mnb_model.pkl'),
        ]
        
        for tfidf_path, model_path in possible_locations:
            if os.path.exists(tfidf_path) and os.path.exists(model_path):
                return tfidf_path, model_path
        
        return None, None
    
    @staticmethod
    def validate_models(tfidf, model):
        """Validate that loaded models are correct type and fitted"""
        try:
            # Check if objects are of correct type
            if not isinstance(tfidf, TfidfVectorizer):
                return False, "TF-IDF object is not a valid TfidfVectorizer"
            
            if not isinstance(model, MultinomialNB):
                return False, "Model object is not a valid MultinomialNB classifier"
            
            # Check if models are fitted by testing with a sample
            test_text = ["test message"]
            try:
                # This will fail if tfidf is not fitted
                test_vector = tfidf.transform(test_text)
                # This will fail if model is not fitted
                _ = model.predict(test_vector)
                return True, "Models are valid and fitted"
            except Exception as e:
                return False, f"Models are not properly fitted: {str(e)}"
                
        except Exception as e:
            return False, f"Error validating models: {str(e)}"
    
    @staticmethod
    def load_and_validate_models():
        """Load and validate models with comprehensive error handling"""
        # Find model files
        tfidf_path, model_path = ModelValidator.find_model_files()
        
        if not tfidf_path or not model_path:
            st.error("❌ Model files not found in any expected location!")
            st.markdown("""
            **Expected locations:**
            - `vectorizer.pkl` and `mnb_model.pkl` in root directory
            - `models/vectorizer.pkl` and `models/mnb_model.pkl` in models folder
            
            **Please ensure your model files are available.**
            """)
            st.stop()
        
        try:
            # Load models
            with open(tfidf_path, 'rb') as f:
                tfidf = pickle.load(f)
            
            with open(model_path, 'rb') as f:
                model = pickle.load(f)
            
            # Validate models
            is_valid, message = ModelValidator.validate_models(tfidf, model)
            
            if not is_valid:
                st.error(f"❌ Model validation failed: {message}")
                st.info("💡 Please retrain your models or check if the model files are corrupted.")
                st.stop()
            
            # st.success(f"✅ Models loaded successfully from: {tfidf_path}, {model_path}")
            return tfidf, model
            
        except Exception as e:
            st.error(f"❌ Error loading models: {str(e)}")
            st.markdown("""
            **Possible solutions:**
            1. Check if model files are corrupted
            2. Retrain your models
            3. Ensure models were saved with the same sklearn version
            4. Check file permissions
            """)
            st.stop()