import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

class UIComponents:
    """UI components and styling for the spam classifier app"""
    
    def apply_custom_css(self):
        """Apply custom CSS styling"""
        st.markdown("""
        <style>
        /* Main theme colors */
        :root {
            --primary-color: #1f77b4;
            --secondary-color: #ff7f0e;
            --success-color: #2ca02c;
            --danger-color: #d62728;
            --warning-color: #ff9800;
            --info-color: #17a2b8;
            --dark-color: #343a40;
            --light-color: #f8f9fa;
        }
        
        /* Header styling */
        .main-header {
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .main-header h1 {
            font-size: 3rem;
            margin-bottom: 0.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .main-header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        
        /* Card styling */
        .info-card {
            background: greenlinear-gradient(135deg, #f0f4f8 0%, #e9ecef 100%);
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            border-left: 4px solid var(--primary-color);
            margin: 1rem 0;
        }
        
        .success-card {
            background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
            border-left: 4px solid var(--success-color);
            color: #155724;
        }
        
        .danger-card {
            background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%);
            border-left: 4px solid var(--danger-color);
            color: #721c24;
        }
        
        /* Stats cards */
        .stat-card {
            background: white;
            padding: 1rem;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            border-top: 3px solid var(--primary-color);
        }
        
        .stat-number {
            font-size: 2rem;
            font-weight: bold;
            color: var(--primary-color);
        }
        
        .stat-label {
            color: #666;
            font-size: 0.9rem;
        }
        
        /* Button styling */
        .stButton > button {
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 25px;
            padding: 0.5rem 2rem;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }
        
        /* Text input styling */
        .stTextInput > div > div > input {
            border-radius: 10px;
            border: 2px solid #e0e0e0;
            padding: 10px;
            transition: border-color 0.3s ease;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: var(--primary-color);
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        
        /* Sidebar styling */
        .css-1d391kg {
            background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
        }
        
        /* Footer */
        .footer {
            margin-top: 3rem;
            padding: 2rem;
            background: linear-gradient(90deg, #343a40 0%, #495057 100%);
            color: white;
            text-align: center;
            border-radius: 10px;
        }
        
        .footer a {
            color: #ffc107;
            text-decoration: none;
            font-weight: bold;
        }
        
        .footer a:hover {
            color: #fff;
        }
        
        /* Animation */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .fade-in {
            animation: fadeIn 0.6s ease-out;
        }
        </style>
        """, unsafe_allow_html=True)
    
    def show_header(self, title, subtitle):
        """Display main header"""
        st.markdown(f"""
        <div class="main-header fade-in">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """, unsafe_allow_html=True)
    
    def show_info_card(self, content, card_type="info"):
        """Display information card"""
        st.markdown(f"""
        <div class="info-card {card_type}-card fade-in">
            {content}
        </div>
        """, unsafe_allow_html=True)
    
    def show_prediction_result(self, result, confidence=None):
        """Display prediction result with styling"""
        if result == 0:  # Not Spam
            icon = "✅"
            message = "Not Spam"
            card_type = "success"
            description = "This message appears to be legitimate and safe."
        else:  # Spam
            icon = "⚠️"
            message = "Spam Detected"
            card_type = "danger"
            description = "This message has been identified as potential spam."
        
        content = f"""
        <div style="text-align: center;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">{icon}</div>
            <h2 style="margin-bottom: 1rem;">{message}</h2>
            <p style="font-size: 1.1rem; margin-bottom: 1rem;">{description}</p>
        """
        
        if confidence:
            content += f'<p><strong>Confidence:</strong> {confidence:.2%}</p>'
        
        content += "</div>"
        
        self.show_info_card(content, card_type)
    
    def show_stats_cards(self, stats):
        """Display statistics in card format"""
        if not stats:
            return
        
        cols = st.columns(4)
        
        stat_items = [
            ("Word Count", stats.get("word_count", 0)),
            ("Characters", stats.get("original_length", 0)),
            ("Sentences", stats.get("sentence_count", 0)),
            ("Numbers", stats.get("number_count", 0))
        ]
        
        for col, (label, value) in zip(cols, stat_items):
            with col:
                st.markdown(f"""
                <div class="stat-card">
                    <div class="stat-number">{value}</div>
                    <div class="stat-label">{label}</div>
                </div>
                """, unsafe_allow_html=True)
    
    def create_confidence_chart(self, confidence):
        """Create confidence visualization"""
        fig = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=confidence * 100,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Prediction Confidence"},
            delta={'reference': 50},
            gauge={
                'axis': {'range': [None, 100]},
                'bar': {'color': "#667eea"},
                'steps': [
                    {'range': [0, 50], 'color': "lightgray"},
                    {'range': [50, 80], 'color': "yellow"},
                    {'range': [80, 100], 'color': "green"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90
                }
            }
        ))
        
        fig.update_layout(height=300)
        return fig
    
    def show_footer(self):
        """Display footer"""
        st.markdown("""
        <div class="footer">
            <p>🛡️ Smart Spam Classifier | Built with ❤️ using Streamlit</p>
            <p><a href="https://ashokumar.in" target="_blank">About Developer</a> | 
               <a href="#" onclick="alert('Contact: your-email@example.com')">Contact</a></p>
            <p><small>© 2024 All rights reserved</small></p>
        </div>
        """, unsafe_allow_html=True)