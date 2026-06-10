import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from styles.home_style import apply_home_style


def render_home(images: dict):
    """
    Renders the landing / home page.
    Parameters : images : dict - Dict returned by image_utils.load_all_images().
    """
    apply_home_style()

    img1 = images["img1"]
    img2 = images["img2"]
    img3 = images["img3"]

    # Hero  
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        <h1 style="font-size:64px; color:#e6f1ff; margin-top:40px;">
        AI-Powered<br>Phishing Detection
        </h1>
        """, unsafe_allow_html=True)

        st.markdown("<br><br>", unsafe_allow_html=True)

        st.markdown("""
        <p style="font-size:18px; color:#8892b0;">
        Detect malicious emails and URLs in real-time using machine learning and
        cybersecurity intelligence.<br>
        PhishGuard AI analyzes emails and URLs using intelligent feature extraction
        and machine learning models.<br>
        Get instant results with clear explanations so you understand why something
        is suspicious.<br>
        </p>
        """, unsafe_allow_html=True)

    with col2:
        st.image("frontend/icons/hacker.png", width=500)

    st.markdown("</div>", unsafe_allow_html=True)

    # Features 
    st.markdown('<h2 style="color:#64ffda;">Features</h2>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("frontend/icons/confidential-email.png", width=60)
        st.markdown('<h4 style="color:#ccd6f6;">Email Analysis</h4>', unsafe_allow_html=True)
        st.markdown(
            "Analyze email content using AI and cybersecurity rules to identify phishing "
            "attempts. Detects patterns like urgency, suspicious intent, and deceptive "
            "messaging techniques used in real-world attacks."
        )

    with col2:
        st.image("frontend/icons/browsing.png", width=60)
        st.markdown('<h4 style="color:#ccd6f6;">URL Analysis</h4>', unsafe_allow_html=True)
        st.markdown(
            "Evaluate URLs for phishing indicators such as suspicious domains, misleading "
            "structures, and hidden threats. Helps identify unsafe links before you click them."
        )

    with col3:
        st.image("frontend/icons/compliance.png", width=60)
        st.markdown('<h4 style="color:#ccd6f6;">Explainable Results</h4>', unsafe_allow_html=True)
        st.markdown(
            "Get instant predictions along with clear reasons behind each decision. "
            "Understand *why* something is flagged as phishing, improving awareness and trust."
        )

    st.markdown("<br><br>", unsafe_allow_html=True)

    # How It Works
    st.markdown('<h2 style="color:#64ffda;">How It Works</h2>', unsafe_allow_html=True)

    st.markdown(f"""
    <style>
      .flow-container {{
        display: flex; align-items: center;
        justify-content: space-between; margin-top: 30px;
      }}
      .flow-box {{
        background: rgba(100,255,218,0.08);
        border: 1px solid rgba(100,255,218,0.3);
        padding: 20px; border-radius: 12px;
        text-align: left; width: 30%; color: #e6f1ff;
        backdrop-filter: blur(10px); transition: 0.3s;
      }}
      .flow-box:hover {{
        transform: scale(1.05);
        box-shadow: 0px 0px 30px rgba(100,255,218,0.4);
      }}
      .arrow {{ font-size: 28px; color: #64ffda; margin: 0 10px; }}
      .icon  {{ margin-bottom: 10px; }}
    </style>

    <div class="flow-container">

      <div class="flow-box">
        <img src="data:image/png;base64,{img1}" width="50" class="icon">
        <h4 style="color:#ccd6f6">Enter Input</h4>
        <p>Paste an email or URL you want to analyze.<br>
           The system accepts raw text, links, or suspicious content.<br>
           Designed for quick and easy user interaction.</p>
      </div>

      <div class="arrow">➜</div>

      <div class="flow-box">
        <img src="data:image/png;base64,{img2}" width="50" class="icon">
        <h4 style="color:#ccd6f6">AI Analysis</h4>
        <p>The model extracts features like keywords, links, and structure.<br>
           It analyzes behavioral patterns and phishing indicators.<br>
           Uses trained ML algorithms to detect threats.</p>
      </div>

      <div class="arrow">➜</div>

      <div class="flow-box">
        <img src="data:image/png;base64,{img3}" width="50" class="icon">
        <h4 style="color:#ccd6f6">Results</h4>
        <p>Instantly classifies input as safe or phishing.<br>
           Provides confidence score and risk indicators.<br>
           Explains the reasoning behind the prediction.</p>
      </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Why Phishing Matters
    st.markdown("""
    <div class="phishing-box">
      <h2 style="color:#64ffda; margin-bottom:10px;">Why Phishing Matters</h2>
      <p class="main-text">
        Phishing attacks remain one of the most common and dangerous cyber threats
        worldwide. Millions of users fall victim to deceptive emails and malicious
        links every year, leading to data theft, financial loss, and security breaches.
      </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="phishing-box">
          <div class="stat-card">
            <div class="stat-number">90%</div>
            <div class="stat-text">of cyberattacks begin with phishing emails</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="phishing-box">
          <div class="stat-card">
            <div class="stat-number">85%</div>
            <div class="stat-text">of users click suspicious links without verification</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="phishing-box">
          <div class="stat-card">
            <div class="stat-number">3.4B</div>
            <div class="stat-text">phishing emails are sent globally every day</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:50px'></div>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Phishing Trends Chart
    st.markdown('<h4 style="color:#64ffda;">Global Phishing Trends</h4>', unsafe_allow_html=True)
    st.markdown(
        '<p style="color:#8892b0;">Based on reports from the Anti-Phishing Working Group (APWG).</p>',
        unsafe_allow_html=True
    )

    data = {
        "Year":    ["2020", "2021", "2022", "2023", "2024", "2025"],
        "Attacks": [1.0, 3.2, 4.1, 4.5, 4.8, 3.8],
    }
    df = pd.DataFrame(data)

    fig, ax = plt.subplots(figsize=(4, 2.5))
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")
    ax.bar(df["Year"], df["Attacks"])
    ax.set_title("Phishing Growth", fontsize=10, color="#ccd6f6")
    ax.set_xlabel("Year", fontsize=8, color="#ccd6f6")
    ax.set_ylabel("Attacks (M)", fontsize=8, color="#ccd6f6")
    ax.tick_params(axis="x", colors="#8892b0", labelsize=8)
    ax.tick_params(axis="y", colors="#8892b0", labelsize=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_color("#8892b0")
    ax.spines["left"].set_color("#8892b0")
    plt.tight_layout()

    chart_col, _, insight_col = st.columns([1, 0.3, 1])

    with chart_col:
        st.pyplot(fig)

    with insight_col:
        st.markdown("""
        <div style="color:#ccd6f6; line-height:1.8;">
          <h3 style="color:#64ffda;">Insights</h3>
          <ul>
            <li>Phishing attacks have surged globally, reaching record volumes across industries.</li>
            <li>APWG reports show 2024 recorded one of the highest phishing levels ever observed.</li>
            <li>Financial services, e-commerce, and SaaS remain primary targets.</li>
            <li>Techniques now include AI-generated emails and realistic impersonation.</li>
            <li>The scale highlights the urgent need for automated detection systems.</li>
          </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Start button
    _, btn_col, _ = st.columns([2, 0.5, 2])

    with btn_col:
        if st.button("Start", key="start_btn"):
            st.session_state.page = "analyze"
            st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div style="
        margin-top: 60px;
        padding: 20px 0;
        border-top: 1px solid rgba(255,255,255,0.1);
        text-align: center;
        color: #8892b0;
        font-size: 14px;
    ">
      © 2026 PhishGuard AI • Built with AI + Cybersecurity
    </div>
    """, unsafe_allow_html=True)