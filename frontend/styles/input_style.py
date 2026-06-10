import streamlit as st


def apply_input_page_style():
    """Inject CSS for the 'Analyze Email / URL' input page."""

    st.markdown("""
    <style>

    html, body, .main { overflow: hidden !important; }

    .block-container {
        padding-top:    0rem !important;
        padding-bottom: 2rem !important;
        max-width: 100% !important;
    }

    /* Text area */
    .stTextArea textarea {
        background:    rgba(17,34,64,0.75) !important;
        color:         #e6f1ff !important;
        border:        1px solid rgba(100,255,218,0.35) !important;
        border-radius: 18px !important;
        padding:       20px !important;
        font-size:     18px !important;
        min-height:    150px !important;
        box-shadow:    0px 0px 20px rgba(100,255,218,0.08);
    }

    /* Analyze button */
    div.stButton > button {
        background: linear-gradient(
            135deg,
            rgba(100,255,218,0.18),
            rgba(100,255,218,0.08)
        ) !important;
        border:        1px solid rgba(100,255,218,0.5) !important;
        color:         #64ffda !important;
        height:        58px !important;
        border-radius: 14px !important;
        font-size:     20px !important;
        font-weight:   600 !important;
        transition:    0.3s !important;
        box-shadow:    0px 0px 22px rgba(100,255,218,0.15);
    }

    div.stButton > button:hover {
        transform:  translateY(-2px);
        border:     1px solid #64ffda !important;
        box-shadow: 0px 0px 30px rgba(100,255,218,0.35);
        color:      white !important;
    }

    </style>
    """, unsafe_allow_html=True)