import streamlit as st


def apply_analyze_page_style():
    """Inject CSS for the 'Choose Analysis Type' page."""

    st.markdown("""
    <style>

    /* Glowing circles  */
    .glow-circle {
        width: 150px; height: 150px;
        border-radius: 50%;
        margin: auto;
        display: flex; align-items: center; justify-content: center;
        border: 4px solid #64ffda;
        box-shadow:
            0px 0px 30px rgba(100,255,218,0.5),
            0px 0px 60px rgba(100,255,218,0.18);
        margin-bottom: 30px;
    }

    .glow-circle-blue {
        width: 150px; height: 150px;
        border-radius: 50%;
        margin: auto;
        display: flex; align-items: center; justify-content: center;
        border: 4px solid #2ea8ff;
        box-shadow:
            0px 0px 30px rgba(46,168,255,0.5),
            0px 0px 60px rgba(46,168,255,0.18);
        margin-bottom: 30px;
    }

    /* Card text  */
    .card-title {
        color: #e6f1ff;
        font-size: 35px;
        font-weight: 500;
        margin-top: 10px;
    }

    .card-desc {
        color: #8892b0;
        font-size: 20px;
        line-height: 1.9;
        margin-top: 25px;
        padding-left: 15px;
        padding-right: 15px;
    }

    /* Scan buttons */
    div.stButton > button {
        background: linear-gradient(
            135deg,
            rgba(100,255,218,0.18),
            rgba(100,255,218,0.08)
        ) !important;
        border: 1px solid rgba(100,255,218,0.5) !important;
        color: #64ffda !important;
        height: 58px !important;
        width: 100px !important;
        border-radius: 14px !important;
        font-size: 20px !important;
        font-weight: 600 !important;
        transition: 0.3s !important;
        box-shadow: 0px 0px 22px rgba(100,255,218,0.15);
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
        border: 1px solid #64ffda !important;
        box-shadow: 0px 0px 30px rgba(100,255,218,0.35);
        color: white !important;
    }

    </style>
    """, unsafe_allow_html=True)