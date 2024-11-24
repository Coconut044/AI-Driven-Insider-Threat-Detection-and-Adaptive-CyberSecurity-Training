import streamlit as st
import importlib.util
import sys
import os

# Configure the page
st.set_page_config(
    page_title="SentinelSecure",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject custom CSS
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

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

class PageConfig:
    """Class to store and manage page configuration settings"""
    _instance = None
    
    def __init__(self):
        if PageConfig._instance is not None:
            raise Exception("PageConfig is a singleton!")
        PageConfig._instance = self
        self.config_set = True
    
    @staticmethod
    def get_instance():
        if PageConfig._instance is None:
            PageConfig()
        return PageConfig._instance

def load_py_file(file_path):
    """Load and execute a Python file without allowing it to set page config"""
    # Add back button at the top
    if st.button("Back", key='back_button'):
        st.session_state.page = 'home'
    
    # Get the file name without extension
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    
    # Import and run the Python file
    spec = importlib.util.spec_from_file_location(file_name, file_path)
    module = importlib.util.module_from_spec(spec)
    
    module.st = st
    
    original_set_page_config = st.set_page_config
    st.set_page_config = lambda *args, **kwargs: None
    
    try:
        sys.modules[file_name] = module
        spec.loader.exec_module(module)
        
        if hasattr(module, 'main'):
            module.main()
        else:
            entry_point_found = False
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if callable(attr) and attr_name.lower().startswith(('run', 'app', 'start', 'main')):  # This triggers the page execution
                    attr()
                    entry_point_found = True
                    break
            
            if not entry_point_found:
                module.__dict__.get('__builtins__', {}).update({'st': st})
                
    except Exception as e:
        st.error(f"Error loading {file_name}: {str(e)}")
    finally:
        st.set_page_config = original_set_page_config

def show_home_page():
    """Display the home page content"""
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
            st.session_state.page = 'threat_detection'  # Set the page to threat_detection

    with col2:
        st.markdown("""
            <div class="button-card">
                <span class="emoji-icon">✨</span>
                <h3 class="card-title">Cybersecurity Training</h3>
                <p class="card-description">
                    Adaptive learning modules designed to strengthen employee security skills through dynamic quizzes.
                </p>
            </div>
        """, unsafe_allow_html=True)

        if st.button('Launch Training', key='launch-btn-2'):
            st.session_state.page = 'training'  # Set the page to training

# Main page routing
if st.session_state.page == 'home':
    show_home_page()
elif st.session_state.page == 'threat_detection':
    load_py_file(r"C:\Users\Nitya\Downloads\SentinelSecure\Employee App.py")
elif st.session_state.page == 'training':
    load_py_file(r"C:\Users\Nitya\Downloads\SentinelSecure\New_Main_Page.py")
