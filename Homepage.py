import streamlit as st
import os

# Initialize session state for navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

# Configure the page
st.set_page_config(
    page_title="SentinelSecure",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS (keeping exactly the same as original)
st.markdown("""
<style>
    /* Main page styling */
    .stApp {
        background: linear-gradient(125deg, #242b75 0%, #1a1f52 100%);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    [data-testid="stHeader"] {
        background: transparent;
    }
    
    .big-title {
        font-family: 'Inter', sans-serif;
        color: #5dbfd5;
        font-size: 5.5rem !important;
        font-weight: 900 !important;
        margin-bottom: 0 !important;
        line-height: 1.1 !important;
        text-align: center !important;
        letter-spacing: -2px;
        text-shadow: 
            0 0 30px rgba(93, 191, 213, 0.5),
            0 0 60px rgba(93, 191, 213, 0.3);
        animation: glow 3s ease-in-out infinite alternate;
    }

    @keyframes glow {
        0% { text-shadow: 0 0 30px rgba(93, 191, 213, 0.5); }
        100% { text-shadow: 0 0 30px rgba(93, 191, 213, 0.8), 0 0 60px rgba(93, 191, 213, 0.6); }
    }

    .subtitle {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(to right, #5dbfd5, #ffffff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 1.6rem !important;
        text-align: center !important;
        margin: 1rem 0 3rem 0 !important;
        font-weight: 500 !important;
        letter-spacing: -0.5px;
    }
    
    .button-card {
        cursor: pointer;
        border-radius: 24px;
        padding: 2.5rem 2rem;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(93, 191, 213, 0.2);
        margin: 1rem;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        overflow: hidden;
        position: relative;
    }
    
    .button-card:hover {
        transform: translateY(-8px) scale(1.02);
        border: 1px solid rgba(93, 191, 213, 0.4);
        box-shadow: 
            0 10px 30px rgba(0, 0, 0, 0.1),
            0 0 40px rgba(93, 191, 213, 0.2);
    }

    .emoji-icon {
        font-size: 3rem !important;
        margin-bottom: 1rem !important;
        text-align: center;
        display: block;
        animation: bounce 2s infinite;
    }

    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    .card-title {
        color: #5dbfd5 !important;
        font-size: 2rem !important;
        font-weight: 700 !important;
        margin-bottom: 1rem !important;
        text-align: center;
        letter-spacing: -0.5px;
    }

    .card-description {
        color: rgba(255, 255, 255, 0.9) !important;
        font-size: 1.1rem !important;
        margin-bottom: 1.5rem !important;
        text-align: center;
        line-height: 1.6 !important;
    }

    /* Button styling */
    .launch-button {
        font-size: 1.2rem !important;
        background: linear-gradient(120deg, #33ccff, #191970);
        color: white !important;
        border: none !important;
        padding: 1rem 2rem !important;
        border-radius: 8px !important;
        cursor: pointer !important;
        display: block;
        margin: 2rem auto;
        transition: 0.3s ease;
    }

    .launch-button:hover {
        background: linear-gradient(120deg, #191970, #33ccff);
        transform: scale(1.05);
    }

</style>
""", unsafe_allow_html=True)

def show_home():
    st.markdown('<h1 class="big-title">SentinelSecure</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">AI Driven Insider Threat Detection and Adaptive CyberSecurity Training</p>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("""
            <div class="button-card">
                <span class="emoji-icon">🛡️</span>
                <h3 class="card-title">Insider Threat Detection</h3>
                <p class="card-description">
                    Supercharged AI defense system that spots suspicious activity in real-time. 
                    Stay one step ahead of potential threats with our cutting-edge detection engine.
                </p>
            </div>
        """, unsafe_allow_html=True)

        if st.button('Launch Threat Detection', key='launch-btn-1'):
            st.session_state.current_page = 'threat_detection'
            st.experimental_rerun()

    with col2:
        st.markdown("""
            <div class="button-card">
                <span class="emoji-icon">✨</span>
                <h3 class="card-title">Adaptive Security Training</h3>
                <p class="card-description">
                    Level up your security game with personalized training that adapts to your style. 
                    Interactive modules that make cybersecurity learning actually fun!
                </p>
            </div>
        """, unsafe_allow_html=True)

        if st.button('Launch Security Training', key='launch-btn-2'):
            st.session_state.current_page = 'security_training'
            st.experimental_rerun()

def show_threat_detection():
    # Import and run the Employee App
    import sys
    sys.path.append(r"C:\Users\Nitya\Downloads\SentinelSecure\Employee App.py")
    import Employee_App
    
    # Add back button at the top
    if st.button('← Back to Home', key='back-btn-1'):
        st.session_state.current_page = 'home'
        st.experimental_rerun()
    
    # Run the app's main content
    Employee_App.main()  # You'll need to modify Employee_App.py to have a main() function

def show_security_training():
    # Import and run the Security Training App
    import sys
    sys.path.append(r"C:\Users\Nitya\Downloads\SentinelSecure\New_Main_Page.py")
    import New_Main_Page
    
    # Add back button at the top
    if st.button('← Back to Home', key='back-btn-2'):
        st.session_state.current_page = 'home'
        st.experimental_rerun()
    
    # Run the app's main content
    New_Main_Page.main()  # You'll need to modify New_Main_Page.py to have a main() function

# Main navigation logic
if st.session_state.current_page == 'home':
    show_home()
elif st.session_state.current_page == 'threat_detection':
    show_threat_detection()
elif st.session_state.current_page == 'security_training':
    show_security_training()
