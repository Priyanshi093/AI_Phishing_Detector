import streamlit as st


def apply_result_page_style():
    """Inject CSS for the Detection Result page."""
    st.markdown("""
    <style>

    html, body { overflow: hidden !important; }

    .block-container {
        padding-top:    0rem;
        padding-bottom: 0rem;
        max-width:      1400px;
    }

    /* Result card */
    .result-card {
        background:     rgba(17,34,64,0.75);
        border:         1px solid rgba(100,255,218,0.15);
        border-radius:  24px;
        padding:        28px;
        backdrop-filter: blur(12px);
    }

    /* Risk circle */
    .risk-circle {
        width:  180px;
        height: 180px;
        border-radius: 50%;
        border: 10px solid #ff5a67;
        display: flex;
        flex-direction:  column;
        justify-content: center;
        align-items:     center;
        margin: auto;
        box-shadow: 0px 0px 30px rgba(255,90,103,0.25);
    }

    /* Reason boxes */
    .reason-box {
        background:    rgba(17,34,64,0.55);
        border-radius: 16px;
        padding:       16px;
        margin-bottom: 10px;
    }

    /* Check Another button */
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
        font-size:     18px !important;
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