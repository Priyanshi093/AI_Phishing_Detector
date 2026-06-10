import streamlit as st


def apply_home_style():
    """Inject CSS specific to the Home / landing page."""
    st.markdown("""
    <style>

    /* ── Hero section ───────────────────────── */
    .hero-container {
        min-height: 80vh;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 120px 80px;
    }

    .hero-title {
        font-size: 64px;
        font-weight: 800;
        color: #e6f1ff;
    }

    .hero-sub {
        margin-top: 20px;
        font-size: 18px;
        color: #8892b0;
        max-width: 500px;
    }

    .hero-right img {
        width: 450px;
        opacity: 0.95;
        filter: drop-shadow(0px 0px 25px rgba(100,255,218,0.4));
    }

    /* ── Image glow ─────────────────────────── */
    img {
        filter: drop-shadow(0px 0px 30px rgba(100,255,218,0.60));
    }

    /* ── Flow / How It Works ────────────────── */
    .flow-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-top: 30px;
    }

    .flow-box {
        background: rgba(100,255,218,0.08);
        border: 1px solid rgba(100,255,218,0.3);
        padding: 20px;
        border-radius: 12px;
        text-align: left;
        width: 30%;
        color: #e6f1ff;
        backdrop-filter: blur(10px);
        transition: 0.3s;
    }

    .flow-box:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 30px rgba(100,255,218,0.4);
    }

    .arrow { font-size: 28px; color: #64ffda; margin: 0 10px; }
    .icon  { margin-bottom: 10px; }

    /* ── Stats / Phishing Matters ───────────── */
    .phishing-box {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 22px;
        padding: 35px;
        margin-top: 20px;
        margin-bottom: 40px;
        backdrop-filter: blur(10px);
    }

    .stat-card   { text-align: center; }

    .stat-number {
        font-size: 34px;
        font-weight: bold;
        color: #64ffda;
    }

    .stat-text {
        color: #ccd6f6;
        font-size: 15px;
        line-height: 1.6;
    }

    .main-text {
        color: #8892b0;
        font-size: 17px;
        line-height: 1.8;
        margin-top: 10px;
    }

    /* Start button */
    div.stButton > button {
        margin-top: 10px;
        background: #64ffda;
        border: none;
        font-size: 20px;
        color: black;
        height: 58px !important;
        width: 100px !important;
        border-radius: 12px;
        font-weight: bold;
    }

    div.stButton > button:hover {
        background: #64ffda;
        color: black;
    }

    /*  Responsive  */
    @media (max-width: 900px) {
        .hero-container { flex-direction: column; text-align: center; }
    }

    </style>
    """, unsafe_allow_html=True)