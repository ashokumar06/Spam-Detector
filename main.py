import streamlit as st
import pickle
from utils.text_processor import TextProcessor
from utils.ui_components import UIComponents
from utils.model_validator import ModelValidator
from all_pages import about, home, analytics, contact

# Page configuration
st.set_page_config(
    page_title="Smart Spam Classifier",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load models and initialize components
@st.cache_resource
def load_models():
    """Load pre-trained models with caching and validation"""
    return ModelValidator.load_and_validate_models()

def main():
    # Load models
    tfidf, model = load_models()
    
    # Initialize components
    text_processor = TextProcessor()
    ui_components = UIComponents()
    
    # Apply custom CSS
    ui_components.apply_custom_css()
    
    # Sidebar navigation
    st.sidebar.title("🛡️ Navigation")
    page = st.sidebar.selectbox(
        "Choose a page:",
        ["🏠 Home", "📊 Analytics", "ℹ️ About", "📞 Contact"]
    )
    
    # Route to different pages
    if page == "🏠 Home":
        home.show_page(tfidf, model, text_processor, ui_components)
    elif page == "📊 Analytics":
        analytics.show_page()
    elif page == "ℹ️ About":
        about.show_page()
    elif page == "📞 Contact":
        contact.show_page()
    
    # Footer
    ui_components.show_footer()

if __name__ == "__main__":
    main()