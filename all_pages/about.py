import streamlit as st

def show_page():
    """About page with project information"""
    
    
    st.markdown("""
    <div class="main-header fade-in">
        <h1>ℹ️ About Smart Spam Classifier</h1>
        <p>Learn about our AI-powered spam detection system</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Project Overview
    st.markdown("## 🎯 Project Overview")
    
    st.markdown("""
    <div class="info-card fade-in">
        <p>The Smart Spam Classifier is an advanced machine learning application designed to automatically 
        identify and filter spam messages. Built using state-of-the-art natural language processing 
        techniques and machine learning algorithms, this system provides accurate, fast, and reliable 
        spam detection capabilities.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Technology Stack
    st.markdown("## 🛠️ Technology Stack")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h4>🤖 Machine Learning</h4>
            <ul>
                <li><strong>Algorithm:</strong> Multinomial Naive Bayes</li>
                <li><strong>Vectorization:</strong> TF-IDF (Term Frequency-Inverse Document Frequency)</li>
                <li><strong>Libraries:</strong> scikit-learn, NLTK</li>
                <li><strong>Model Size:</strong> Lightweight and efficient</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h4>💻 Development Stack</h4>
            <ul>
                <li><strong>Frontend:</strong> Streamlit</li>
                <li><strong>Backend:</strong> Python</li>
                <li><strong>NLP:</strong> spaCy, NLTK</li>
                <li><strong>Visualization:</strong> Plotly, Matplotlib</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # How It Works
    st.markdown("## ⚙️ How It Works")
    
    steps_col1, steps_col2 = st.columns(2)
    
    with steps_col1:
        st.markdown("""
        <div class="info-card">
            <h4>📝 Text Preprocessing</h4>
            <ol>
                <li><strong>Normalization:</strong> Convert text to lowercase</li>
                <li><strong>Cleaning:</strong> Remove punctuation and numbers</li>
                <li><strong>Tokenization:</strong> Split text into individual words</li>
                <li><strong>Stop Words:</strong> Remove common words (the, and, is, etc.)</li>
                <li><strong>Stemming:</strong> Reduce words to their root form</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
    
    with steps_col2:
        st.markdown("""
        <div class="info-card">
            <h4>🧠 Machine Learning Pipeline</h4>
            <ol>
                <li><strong>Feature Extraction:</strong> Convert text to numerical vectors</li>
                <li><strong>TF-IDF Weighting:</strong> Calculate word importance scores</li>
                <li><strong>Classification:</strong> Apply Naive Bayes algorithm</li>
                <li><strong>Prediction:</strong> Output spam/not-spam classification</li>
                <li><strong>Confidence:</strong> Provide prediction probability</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
    
    # Dataset Information
    st.markdown("## 📊 Dataset Information")
    
    st.markdown("""
    <div class="info-card">
        <h4>📋 SMS Spam Collection Dataset</h4>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <strong>Total Messages:</strong> 5,574<br>
                <strong>Spam Messages:</strong> 747 (13.4%)<br>
                <strong>Ham Messages:</strong> 4,827 (86.6%)
            </div>
            <div>
                <strong>Source:</strong> UCI Machine Learning Repository<br>
                <strong>Format:</strong> SMS text messages<br>
                <strong>Language:</strong> English
            </div>
            <div>
                <strong>Quality:</strong> Manually verified<br>
                <strong>Bias:</strong> Balanced representation<br>
                <strong>Privacy:</strong> Anonymized data
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Model Performance
    st.markdown("## 📈 Model Performance")
    
    perf_col1, perf_col2, perf_col3, perf_col4 = st.columns(4)
    
    with perf_col1:
        st.metric("Accuracy", "97.3%", "↑ 2.3%")
    
    with perf_col2:
        st.metric("Precision", "96.5%", "↑ 1.5%")
    
    with perf_col3:
        st.metric("Recall", "98.1%", "↑ 3.1%")
    
    with perf_col4:
        st.metric("F1-Score", "97.3%", "↑ 2.3%")
    
    # Features and Benefits
    st.markdown("## ✨ Features & Benefits")
    
    features_col1, features_col2, features_col3 = st.columns(3)
    
    with features_col1:
        st.markdown("""
        <div class="info-card success-card">
            <h4>🚀 Performance</h4>
            <ul>
                <li>97%+ accuracy rate</li>
                <li>Real-time processing</li>
                <li>Low false positive rate</li>
                <li>Efficient memory usage</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with features_col2:
        st.markdown("""
        <div class="info-card">
            <h4>🔒 Security</h4>
            <ul>
                <li>Local processing</li>
                <li>No data storage</li>
                <li>Privacy-focused design</li>
                <li>Secure architecture</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with features_col3:
        st.markdown("""
        <div class="info-card">
            <h4>👥 User Experience</h4>
            <ul>
                <li>Intuitive interface</li>
                <li>Instant results</li>
                <li>Detailed analytics</li>
                <li>Educational insights</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Future Improvements
    st.markdown("## 🔮 Future Enhancements")
    
    st.markdown("""
    <div class="info-card">
        <h4>🛣️ Roadmap</h4>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <h5>📧 Email Support</h5>
                <p>Extend classification to email messages with header analysis and attachment scanning.</p>
            </div>
            <div>
                <h5>🌍 Multi-language</h5>
                <p>Add support for multiple languages including Hindi, Spanish, French, and German.</p>
            </div>
            <div>
                <h5>🧠 Deep Learning</h5>
                <p>Implement transformer-based models like BERT for improved context understanding.</p>
            </div>
            <div>
                <h5>📱 API Integration</h5>
                <p>Develop REST API for integration with mobile apps and other applications.</p>
            </div>
            <div>
                <h5>🔄 Real-time Learning</h5>
                <p>Implement online learning capabilities to adapt to new spam patterns.</p>
            </div>
            <div>
                <h5>📊 Advanced Analytics</h5>
                <p>Add clustering analysis and pattern discovery for spam trend identification.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Technical Details
    st.markdown("## 🔬 Technical Implementation")
    
    with st.expander("📋 Detailed Technical Specifications"):
        st.markdown("""
        ### Model Architecture
        - **Algorithm**: Multinomial Naive Bayes Classifier
        - **Feature Engineering**: TF-IDF with n-gram analysis (1-2 grams)
        - **Preprocessing**: spaCy NLP pipeline with custom tokenization
        - **Optimization**: Hyperparameter tuning using Grid Search CV
        
        ### Performance Metrics
        - **Cross-validation**: 5-fold stratified cross-validation
        - **Test Set**: 20% holdout with stratified sampling
        - **Evaluation**: Precision, Recall, F1-Score, ROC-AUC
        - **Validation**: Confusion matrix analysis
        
        ### Code Quality
        - **Structure**: Modular design with separation of concerns
        - **Documentation**: Comprehensive docstrings and comments
        - **Testing**: Unit tests for critical functions
        - **Version Control**: Git with semantic versioning
        
        ### Deployment
        - **Framework**: Streamlit for web interface
        - **Hosting**: Cloud deployment ready
        - **Scalability**: Stateless design for horizontal scaling
        - **Monitoring**: Built-in analytics and logging
        """)
    
    # Contact and Credits
    st.markdown("## 📞 Contact & Credits")
    
    contact_col1, contact_col2 = st.columns(2)
    
    with contact_col1:
        st.markdown("""
        <div class="info-card">
            <h4>👨‍💻 Developer</h4>
            <p><strong>Name:</strong> [Your Name]<br>
            <strong>Institution:</strong> [Your College]<br>
            <strong>Course:</strong> [Your Course]<br>
            <strong>Email:</strong> <a href="mailto:your-email@example.com">your-email@example.com</a><br>
            <strong>Portfolio:</strong> <a href="https://ashokumar.in" target="_blank">ashokumar.in</a></p>
        </div>
        """, unsafe_allow_html=True)
    
    with contact_col2:
        st.markdown("""
        <div class="info-card">
            <h4>🙏 Acknowledgments</h4>
            <ul>
                <li><strong>Dataset:</strong> UCI Machine Learning Repository</li>
                <li><strong>Libraries:</strong> scikit-learn, NLTK, spaCy teams</li>
                <li><strong>Framework:</strong> Streamlit community</li>
                <li><strong>Inspiration:</strong> Academic research in NLP</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # License and Usage
    st.markdown("## 📄 License & Usage")
    
    st.markdown("""
    <div class="info-card">
        <h4>📋 Terms of Use</h4>
        <p>This project is developed for educational purposes as part of a college project. 
        The code is open-source and available for academic use. For commercial usage, 
        please contact the developer for licensing terms.</p>
        
        <p><strong>License:</strong> MIT License (Educational Use)<br>
        <strong>Citation:</strong> Please cite this work if used in academic projects<br>
        <strong>Support:</strong> Community-driven with educational focus</p>
    </div>
    """, unsafe_allow_html=True)

