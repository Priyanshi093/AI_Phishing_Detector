import streamlit as st

from styles.input_style import apply_input_page_style


def render_input_page():
    """Renders the email / URL text-input page."""

    apply_input_page_style()

    input_type = st.session_state.get("input_type", "Email")

    # Icon
    icon_path = (
        "frontend/icons/secure.png"
        if input_type == "Email"
        else "frontend/icons/secure_browse.png"
    )

    _, icon_col, _ = st.columns([3, 1, 3])
    with icon_col:
        st.image(icon_path, width=100)

    # Title
    title = "Analyze Email" if input_type == "Email" else "Analyze URL"

    st.markdown(f"""
    <h1 style="text-align:center; color:#e6f1ff;
               font-size:50px; margin-top:0px; margin-bottom:8px;">
        {title}
    </h1>
    """, unsafe_allow_html=True)

    # Subtitle
    subtitle = (
        "Paste the email content below and let our AI analyze it<br>"
        "for phishing threats and suspicious indicators."
        if input_type == "Email"
        else
        "Paste the URL below and let our AI analyze it<br>"
        "for phishing threats and suspicious indicators."
    )

    st.markdown(f"""
    <p style="text-align:center; color:#8892b0;
              font-size:24px; line-height:1.5; margin-bottom:10px;">
        {subtitle}
    </p>
    """, unsafe_allow_html=True)

   
    left_space, center_area, right_space = st.columns([1,5,1])

    with center_area:

        label_text = (
         "Paste email content here:"
         if input_type == "Email"
         else "Paste URL here:"
        )

        st.markdown(
        f"""
        <p style="
        color:#64ffda;
        font-size:24px;
        font-weight:600;
        margin-left:0px;
        margin-bottom:10px;
        ">
        {label_text}
        </p>
        """,
        unsafe_allow_html=True
        )

        user_input = st.text_area(
        "",
        height=100,
        placeholder=(
            "Paste the full email content here..."
            if input_type == "Email"
            else "Paste the URL here..."
        ),
        key="email_input_box",
        label_visibility="collapsed"
        )

    # Validation warning 
    if "show_email_warning" not in st.session_state:
        st.session_state.show_email_warning = False

    if st.session_state.show_email_warning:
        warning = "Please enter email text" if input_type == "Email" else "Please enter URL"
        st.markdown(
            f"<p style='color:#ff6b6b; margin-left:550px; margin-top:3px; font-size:16px;'>{warning}</p>",
            unsafe_allow_html=True,
        )

    # Analyze button 
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    _, btn_col, _ = st.columns([2, 1, 2])
    with btn_col:
        clicked = st.button("Analyze", key="analyze_email_button")

    if clicked:
        if not user_input.strip():
            st.session_state.show_email_warning = True
            st.rerun()
        else:
            st.session_state.show_email_warning = False
            st.session_state.input_data = user_input
            st.session_state.page = "result"
            st.rerun()