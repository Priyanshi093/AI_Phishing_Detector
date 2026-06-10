import streamlit as st


def render_header(logo_b64: str):
    """
    Renders the fixed top navigation bar.

    Parameters (logo_b64 : str) - Base-64 encoded logo image (from image_utils.load_all_images()).
    """
    # Inject header CSS 
    st.markdown("""
    <style>

    .top-header {
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 70px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 40px;
        background: rgba(2,12,27,0.95);
        backdrop-filter: blur(10px);
        z-index: 9999;
        border-bottom: 1px solid rgba(255,255,255,0.08);
    }

    .nav-buttons {
        position: fixed;
        top: 14px;
        right: 30px;
        display: flex;
        align-items: center;
        gap: 12px;
        z-index: 10000;
    }

    .nav-buttons div[data-testid="stButton"] { display: inline-block; }

    /* Home button style */
    div.stButton > button {
        background: linear-gradient(
            135deg,
            rgba(100,255,218,0.18),
            rgba(100,255,218,0.08)
        ) !important;
        border:        1px solid rgba(100,255,218,0.5) !important;
        color:         #64ffda !important;
        height:        42px !important;
        width:         100px !important;
        border-radius: 14px !important;
        font-size:     16px !important;
        font-weight:   600 !important;
        margin-top:    30px !important;
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

    # Logo + brand name 
    header_col1, header_col2 = st.columns([12, 1])

    with header_col1:
        st.markdown(f"""
        <div style="
            display: flex;
            align-items: center;
            gap: 12px;
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 70px;
            padding-left: 40px;
            background: rgba(2,12,27,0.95);
            backdrop-filter: blur(10px);
            z-index: 999;
            border-bottom: 1px solid rgba(255,255,255,0.08);
        ">
            <img src="data:image/png;base64,{logo_b64}" width="35">
            <div style="color:#64ffda; font-size:22px; font-weight:600;">
                PhishGuard AI
            </div>

            
        </div>
        """, unsafe_allow_html=True)

    #  Home button 
    with header_col2:
        st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)
        if st.button("Home", key="home_btn"):
            st.session_state.page = "home"
            st.rerun()
        st.markdown('</div>',unsafe_allow_html=True)