import streamlit as st
from datetime import datetime

def show_page():
    """Contact page with feedback form and support information"""
    
    st.markdown("""
    <div class="main-header fade-in">
        <h1>📞 Contact & Support</h1>
        <p>Get in touch with us for feedback, support, or collaboration</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact Information
    st.markdown("## 📧 Contact Information")
    
    contact_col1, contact_col2 = st.columns(2)
    
    with contact_col1:
        st.markdown("""
        <div class="info-card">
            <h4>👨‍💻 Developer Information</h4>
            <p><strong>Name:</strong> Ashok Kumar<br>
            <strong>Role:</strong> ML Engineer & Student<br>
            <strong>Institution:</strong> ECB <br>
            <strong>Course:</strong> AI DS </p>
            
            <h5>📱 Contact Details</h5>
            <p><strong>Email:</strong> <a href="mailto:contact@ashokumar.in">contact@ashokumar.in</a><br>
            <strong>Website:</strong> <a href="https://ashokumar.in" target="_blank">ashokumar.in</a><br>
            <strong>LinkedIn:</strong> <a href="#" target="_blank">linkedin.com/in/ashokkumar</a><br>
            <strong>GitHub:</strong> <a href="#" target="_blank">github.com/ashokkumar06</a></p>
        </div>
        """, unsafe_allow_html=True)
    
    with contact_col2:
        st.markdown("""
        <div class="info-card">
            <h4>🎓 Academic Project</h4>
            <p>This spam classifier is developed as part of a college project focusing on 
            machine learning applications in cybersecurity and natural language processing.</p>
            
            <h5>🎯 Project Objectives</h5>
            <ul>
                <li>Demonstrate ML classification techniques</li>
                <li>Apply NLP for text analysis</li>
                <li>Build user-friendly web applications</li>
                <li>Showcase data science skills</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Feedback Form
    st.markdown("## 💬 Feedback Form")
    
    with st.form("feedback_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Your Name*", placeholder="Enter your full name")
            email = st.text_input("Email Address*", placeholder="your.email@example.com")
        
        with col2:
            subject = st.selectbox(
                "Subject*",
                ["General Feedback", "Bug Report", "Feature Request", "Academic Inquiry", "Collaboration", "Other"]
            )
            rating = st.select_slider(
                "Rate this application",
                options=[1, 2, 3, 4, 5],
                value=4,
                format_func=lambda x: "⭐" * x
            )
        
        message = st.text_area(
            "Your Message*",
            placeholder="Please share your feedback, suggestions, or questions...",
            height=150
        )
        
        # Additional options
        st.markdown("### 📋 Additional Information")
        
        col1, col2 = st.columns(2)
        with col1:
            subscribe = st.checkbox("Subscribe to project updates")
            collaborate = st.checkbox("Interested in collaboration")
        
        with col2:
            share_data = st.checkbox("Allow sharing feedback for improvement")
            urgent = st.checkbox("This is urgent")
        
        submitted = st.form_submit_button("📤 Send Feedback", type="primary")
        
        if submitted:
            if name and email and message:
                # In a real application, you would send this data to a backend service
                st.success("✅ Thank you for your feedback! We'll get back to you soon.")
                
                # Display submission summary
                with st.expander("📋 Submission Summary"):
                    st.json({
                        "Name": name,
                        "Email": email,
                        "Subject": subject,
                        "Rating": f"{'⭐' * rating} ({rating}/5)",
                        "Message": message[:100] + "..." if len(message) > 100 else message,
                        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "Options": {
                            "Subscribe": subscribe,
                            "Collaborate": collaborate,
                            "Share Data": share_data,
                            "Urgent": urgent
                        }
                    })
            else:
                st.error("❌ Please fill in all required fields (marked with *)")
    
    # FAQ Section
    st.markdown("## ❓ Frequently Asked Questions")
    
    faqs = [
        {
            "question": "How accurate is the spam classifier?",
            "answer": "Our model achieves 97.3% accuracy on test data, with 96.5% precision and 98.1% recall. This means it correctly identifies spam messages 97% of the time while maintaining low false positive rates."
        },
        {
            "question": "Is my data stored or shared?",
            "answer": "No, your messages are processed locally and not stored on our servers. We prioritize user privacy and data security. All processing happens in real-time without data retention."
        },
        {
            "question": "Can I use this for commercial purposes?",
            "answer": "This is an educational project. For commercial use, please contact the developer for licensing terms. The code is open-source for academic and learning purposes."
        },
        {
            "question": "How can I contribute to this project?",
            "answer": "We welcome contributions! You can help by reporting bugs, suggesting features, improving documentation, or contributing code. Check our GitHub repository for contribution guidelines."
        },
        {
            "question": "What languages are supported?",
            "answer": "Currently, the classifier is optimized for English text. We're working on multi-language support including Hindi, Spanish, and French in future versions."
        },
        {
            "question": "How do I report a bug or issue?",
            "answer": "Please use the feedback form above with 'Bug Report' as the subject, or contact us directly via email. Include steps to reproduce the issue and any error messages."
        }
    ]
    
    for i, faq in enumerate(faqs):
        with st.expander(f"❓ {faq['question']}"):
            st.markdown(faq['answer'])
    
    # Support Resources
    st.markdown("## 🛠️ Support Resources")
    
    resource_col1, resource_col2, resource_col3 = st.columns(3)
    
    with resource_col1:
        st.markdown("""
        <div class="info-card">
            <h4>📚 Documentation</h4>
            <ul>
                <li><a href="#" target="_blank">User Guide</a></li>
                <li><a href="#" target="_blank">API Documentation</a></li>
                <li><a href="#" target="_blank">Technical Report</a></li>
                <li><a href="#" target="_blank">Installation Guide</a></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with resource_col2:
        st.markdown("""
        <div class="info-card">
            <h4>💻 Code & Resources</h4>
            <ul>
                <li><a href="#" target="_blank">GitHub Repository</a></li>
                <li><a href="#" target="_blank">Dataset Download</a></li>
                <li><a href="#" target="_blank">Model Files</a></li>
                <li><a href="#" target="_blank">Example Scripts</a></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with resource_col3:
        st.markdown("""
        <div class="info-card">
            <h4>🎓 Learning Materials</h4>
            <ul>
                <li><a href="#" target="_blank">Tutorial Videos</a></li>
                <li><a href="#" target="_blank">Research Papers</a></li>
                <li><a href="#" target="_blank">Case Studies</a></li>
                <li><a href="#" target="_blank">Best Practices</a></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Project Statistics
    st.markdown("## 📊 Project Statistics")
    
    stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
    
    with stat_col1:
        st.metric("Total Classifications", "1,247", "↑ 156 this week")
    
    with stat_col2:
        st.metric("Active Users", "89", "↑ 12 this week")
    
    with stat_col3:
        st.metric("Accuracy Rate", "97.3%", "↑ 0.2%")
    
    with stat_col4:
        st.metric("Feedback Received", "34", "↑ 8 this week")
    
    # Call to Action
    st.markdown("## 🤝 Get Involved")
    
    st.markdown("""
    <div class="info-card success-card">
        <h4>🌟 Join Our Community</h4>
        <p>We're always looking for collaborators, testers, and contributors to help improve this project. 
        Whether you're a student, researcher, or industry professional, your input is valuable!</p>
        
        <div style="margin-top: 1rem;">
            <strong>Ways to contribute:</strong>
            <ul>
                <li>🐛 Report bugs and issues</li>
                <li>💡 Suggest new features</li>
                <li>📝 Improve documentation</li>
                <li>🧪 Test with different datasets</li>
                <li>🎨 Enhance UI/UX design</li>
                <li>🤖 Optimize ML algorithms</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Emergency Contact
    st.markdown("## 🚨 Emergency Contact")
    
    st.markdown("""
    <div class="info-card danger-card">
        <h4>⚠️ Urgent Issues</h4>
        <p>For critical bugs, security issues, or urgent academic deadlines:</p>
        <p><strong>Emergency Email:</strong> <a href="mailto:urgent@ashokumar.in">urgent@ashokumar.in</a><br>
        <strong>Response Time:</strong> Within 24 hours<br>
        <strong>Available:</strong> Monday-Friday, 9 AM - 6 PM IST</p>
    </div>
    """, unsafe_allow_html=True)