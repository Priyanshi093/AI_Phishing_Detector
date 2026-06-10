import streamlit as st
import requests

from styles.result_style import apply_result_page_style


def render_result_page():
    """Calls the backend API and renders the Detection Result page."""
    apply_result_page_style()

    # API call to get results from backend
    if st.session_state.input_type == "Email":
        response = requests.post(
            "http://127.0.0.1:5000/predict-email",
            json={"text": st.session_state.input_data},
        )
    else:
        response = requests.post(
            "http://127.0.0.1:5000/predict-url",
            json={"url": st.session_state.input_data},
        )

    data = response.json()

    # Page heading 
    st.markdown("""
    <h1 style="text-align:center; color:white; margin-bottom:0px;">
        Detection Result
    </h1>
    <p style="text-align:center; color:#8892b0; margin-bottom:3px;">
        Here's what our AI found.
    </p>
    """, unsafe_allow_html=True)

    # Score + Result card 
    left, right = st.columns([1, 2])

    with left:
        if st.session_state.input_type == "Email":
            score       = data.get("confidence", 0)
            score_label = "Confidence"
        else:
            score       = data.get("risk_score", 0)
            score_label = "Risk Score"

        st.markdown(f"""
        <div style="text-align:center;">
          <h1 style="color:#64ffda; font-size:50px; margin-bottom:0px;">
            {score}%
          </h1>
          <p style="color:#8892b0; font-size:18px; margin-top:0px;">
            {score_label}
          </p>
        </div>
        """, unsafe_allow_html=True)

    with right:
        result_color = {
            "Phishing": "#ff5a67",
            "Safe":     "#0eec37d3",
        }.get(data["result"], "#f4c508")

        st.markdown(f"""
        <div class="result-card">
          <h2 style="color:{result_color}; margin-bottom:0px;">
            {data['result']}
          </h2>
          <p style="color:#8892b0; font-size:18px; margin-bottom:0px;">
            Analysis completed successfully
          </p>
        </div>
        """, unsafe_allow_html=True)

        colA, colB = st.columns(2)

        with colA:
            st.markdown(
                '<p style="color:#8892b0; margin-bottom:0px;">Type</p>',
                unsafe_allow_html=True,
            )
            st.markdown(
                f'<h2 style="color:#3b82f6; margin-top:0px;">'
                f'{st.session_state.input_type}</h2>',
                unsafe_allow_html=True,
            )

        with colB:
            st.markdown("<br>", unsafe_allow_html=True)

    # Reasons 
    st.markdown(
        '<h3 style="color:white; margin-bottom:0px;">Why this result?</h3>',
        unsafe_allow_html=True,
    )

    for reason in data["reasons"][:3]:
        st.markdown(
            f'<div class="reason-box">{reason}</div>',
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Check Another button 
    _, btn_col, _ = st.columns([2, 1, 2])

    with btn_col:
        if st.button("Check Another", use_container_width=True, key="check_again_btn"):
            st.session_state.page = "analyze"
            st.rerun()