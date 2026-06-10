import streamlit as st
from styles.analyze_style import apply_analyze_page_style


def render_analyze_page(images: dict):
    """
    Renders the 'Choose Analysis Type' page.
    Parameters : (images : dict) -> Dict returned by image_utils.load_all_images().
    """
    apply_analyze_page_style()

    img4 = images["img4"]
    img5 = images["img5"]

    # Page heading 
    st.markdown("""
    <h1 style="
        text-align: center; color: #e6f1ff;
        font-size: 50px; margin-top: 1px;
        margin-bottom: 3px; font-weight: 800;
    ">
        Choose Analysis Type
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="
        text-align: center; color: #8892b0;
        font-size: 22px; margin-bottom: 50px;
    ">
        Select an option below to start scanning and detecting phishing threats
    </p>
    """, unsafe_allow_html=True)

    left, center, right = st.columns([5, 1, 5])

    # Email card 
    with left:
        st.markdown(f"""
        <div class="glow-circle">
          <img src="data:image/png;base64,{img4}" width="105"
               style="filter: drop-shadow(0px 0px 10px #64ffda)
                              drop-shadow(0px 0px 22px #64ffda);">
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <h2 style="color:#e6f1ff; text-align:center;
                   font-size:45px; margin-top:40px;">
            Analyze Email
        </h2>
        """, unsafe_allow_html=True)

        st.markdown("""
        <p style="color:#8892b0; font-size:22px; line-height:2;
                  text-align:center; padding:0px 50px;">
            Scan suspicious emails and detect phishing attempts,
            malicious content, and fake senders using intelligent
            AI-powered analysis.
        </p>
        """, unsafe_allow_html=True)

        st.markdown("<br><br>", unsafe_allow_html=True)

        _, btn_c, _ = st.columns([1, 1, 1])
        with btn_c:
            if st.button("Scan", key="email_analysis_final"):
                st.session_state.input_type = "Email"
                st.session_state.page = "input"
                st.rerun()

    # Divider 
    with center:
        st.markdown("""
        <div style="
            display: flex; flex-direction: column;
            align-items: center; justify-content: center;
            height: 650px;
        ">
          <div style="width:2px; height:160px;
               background:linear-gradient(to bottom,transparent,#64ffda,transparent);
               box-shadow:0px 0px 12px rgba(100,255,218,0.6);"></div>

          <div style="
              width:90px; height:90px; border-radius:50%;
              border:2px solid #64ffda;
              display:flex; align-items:center; justify-content:center;
              color:#64ffda; font-size:32px; font-weight:700;
              margin:18px 0; background:rgba(10,25,47,0.95);
              box-shadow:0px 0px 20px rgba(100,255,218,0.35);
          ">OR</div>

          <div style="width:2px; height:160px;
               background:linear-gradient(to bottom,transparent,#64ffda,transparent);
               box-shadow:0px 0px 12px rgba(100,255,218,0.6);"></div>
        </div>
        """, unsafe_allow_html=True)

    # URL card
    with right:
        st.markdown(f"""
        <div class="glow-circle-blue">
          <img src="data:image/png;base64,{img5}" width="105"
               style="filter: drop-shadow(0px 0px 10px #2ea8ff)
                              drop-shadow(0px 0px 22px #2ea8ff);">
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <h2 style="color:#e6f1ff; text-align:center;
                   font-size:45px; margin-top:40px;">
            Analyze URL
        </h2>
        """, unsafe_allow_html=True)

        st.markdown("""
        <p style="color:#8892b0; font-size:22px; line-height:2;
                  text-align:center; padding:0px 50px;">
            Inspect suspicious URLs and websites for phishing risks,
            malicious redirects, and dangerous domains
            using smart threat detection.
        </p>
        """, unsafe_allow_html=True)

        st.markdown("<br><br>", unsafe_allow_html=True)

        _, btn_c, _ = st.columns([1, 1, 1])
        with btn_c:
            if st.button("Scan", key="url_analysis_final"):
                st.session_state.input_type = "URL"
                st.session_state.page = "input"
                st.rerun()