import streamlit as st


def apply_global_style():
    """Inject global CSS: background, typography, Streamlit chrome removal."""
    st.markdown("""
    <style>

    /* Layout  */
    .stApp { margin: 0; padding: 0; }
    .block-container {
        padding-left:  50px;
        padding-right: 50px;
        padding-top:   0 !important;
    }
    html, body, .main { overflow-x: hidden; }

    /* Hide Streamlit chrome  */
    #MainMenu { visibility: hidden; }
    footer    { visibility: hidden; }
    header    { visibility: hidden; }

    /* Background */
    html, body, .stApp {
        background:
            radial-gradient(circle at 20% 20%, #112240, #020c1b),
            repeating-linear-gradient(
                0deg,
                transparent,
                transparent 1px,
                rgba(100,255,218,0.05) 1px,
                rgba(100,255,218,0.05) 2px
            );
        color: white;
    }

    /* Inputs */
    .stTextInput > div > div > input,
    .stTextArea textarea {
        background-color: #112240;
        color: white;
    }

    </style>
    """, unsafe_allow_html=True)