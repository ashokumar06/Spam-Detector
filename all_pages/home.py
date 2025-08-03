import streamlit as st
import numpy as np
import time

def show_page(tfidf, model, text_processor, ui_components):
    """Main spam classification page"""
    
    # Header
    ui_components.show_header(
        "🛡️ Smart Spam Classifier",
        "Protect yourself from unwanted messages with AI-powered detection"
    )
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📝 Enter Your Message")
        
        # Text input options
        input_method = st.radio(
            "Choose input method:",
            ["✍️ Type Message", "📤 Upload File"],
            horizontal=True
        )
        
        input_text = ""
        
        if input_method == "✍️ Type Message":
            input_text = st.text_area(
                "Enter the message you want to check:",
                height=150,
                placeholder="Type or paste your message here..."
            )
        else:
            uploaded_file = st.file_uploader(
                "Upload a text file:",
                type=['txt'],
                help="Upload a .txt file containing the message to classify"
            )
            if uploaded_file:
                input_text = str(uploaded_file.read(), "utf-8")
                st.text_area("File content:", input_text, height=100, disabled=True)
        
        # Sample messages for testing
        st.markdown("#### 🎯 Try These Examples:")
        col_ex1, col_ex2 = st.columns(2)
        
        with col_ex1:
            if st.button("📧 Normal Message", key="normal"):
                input_text = "Hi there! Hope you're having a great day. Let's meet for coffee tomorrow at 3 PM."
                st.rerun()
        
        with col_ex2:
            if st.button("⚠️ Spam Message", key="spam"):
                input_text = "URGENT! You've won $1000000! Click here NOW to claim your prize! Limited time offer!!!"
                st.rerun()
    
    with col2:
        st.markdown("### 📊 How It Works")
        ui_components.show_info_card("""
        <h4>🔍 Analysis Process:</h4>
        <ol>
            <li><strong>Text Preprocessing:</strong> Clean and normalize text</li>
            <li><strong>Feature Extraction:</strong> Convert text to numerical features</li>
            <li><strong>ML Classification:</strong> Use trained model for prediction</li>
            <li><strong>Result Display:</strong> Show classification with confidence</li>
        </ol>
        """)
        
        # Model information
        st.markdown("### 🤖 Model Info")
        st.info("""
        **Algorithm:** Multinomial Naive Bayes  
        **Features:** TF-IDF Vectorization  
        **Training:** SMS Spam Collection Dataset  
        **Accuracy:** ~97% on test data
        """)
    
    # Prediction section
    if st.button("🔍 Analyze Message", type="primary"):
        if input_text.strip():
            with st.spinner("🔄 Analyzing message..."):
                # Add a small delay for better UX
                time.sleep(1)
                
                try:
                    # Process text
                    transformed_text = text_processor.transform_text(input_text)
                    
                    # Get text statistics
                    text_stats = text_processor.get_text_stats(input_text)
                    
                    # Make prediction
                    vector_input = tfidf.transform([transformed_text])
                    prediction = model.predict(vector_input)[0]
                    prediction_proba = model.predict_proba(vector_input)[0]
                    confidence = max(prediction_proba)
                    
                    # Display results
                    st.markdown("---")
                    st.markdown("## 📋 Analysis Results")
                    
                    # Show prediction result
                    ui_components.show_prediction_result(prediction, confidence)
                    
                    # Show statistics
                    st.markdown("### 📈 Message Statistics")
                    ui_components.show_stats_cards(text_stats)
                    
                    # Detailed analysis
                    col_detail1, col_detail2 = st.columns(2)
                    
                    with col_detail1:
                        st.markdown("#### 🔍 Detailed Analysis")
                        st.json({
                            "Original Length": text_stats.get("original_length", 0),
                            "Processed Length": text_stats.get("processed_length", 0),
                            "Uppercase Characters": text_stats.get("uppercase_count", 0),
                            "Punctuation Count": text_stats.get("punctuation_count", 0),
                            "Classification": "Spam" if prediction == 1 else "Not Spam",
                            "Confidence Score": f"{confidence:.4f}"
                        })
                    
                    with col_detail2:
                        st.markdown("#### 📊 Confidence Visualization")
                        confidence_chart = ui_components.create_confidence_chart(confidence)
                        st.plotly_chart(confidence_chart, use_container_width=True)
                    
                    # Show processed text (for educational purposes)
                    with st.expander("🔧 View Processed Text"):
                        st.text_area(
                            "Processed text (after cleaning, stemming, etc.):",
                            transformed_text,
                            height=100,
                            disabled=True
                        )
                        
                        st.markdown("**Processing Steps Applied:**")
                        st.markdown("""
                        - Converted to lowercase
                        - Removed punctuation and numbers
                        - Tokenized using spaCy
                        - Removed stop words
                        - Applied stemming
                        """)
                
                except Exception as e:
                    st.error(f"❌ An error occurred during prediction: {str(e)}")
        
        else:
            st.warning("⚠️ Please enter some text to classify.")
    
    # Additional features section
    st.markdown("---")
    st.markdown("## 🚀 Additional Features")
    
    feature_cols = st.columns(3)
    
    with feature_cols[0]:
        ui_components.show_info_card("""
        <h4>🎯 High Accuracy</h4>
        <p>Our model achieves 97%+ accuracy using advanced NLP techniques and machine learning algorithms.</p>
        """)
    
    with feature_cols[1]:
        ui_components.show_info_card("""
        <h4>⚡ Fast Processing</h4>
        <p>Get instant results with optimized text processing and efficient model inference.</p>
        """)
    
    with feature_cols[2]:
        ui_components.show_info_card("""
        <h4>🔒 Privacy Focused</h4>
        <p>Your messages are processed locally and not stored or transmitted to external servers.</p>
        """)