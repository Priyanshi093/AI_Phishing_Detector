
# import streamlit as st
# import requests   
# import time

# #img conversion to base64
# import base64

# def get_base64_image(path):
#         with open(path, "rb") as f:
#          return base64.b64encode(f.read()).decode()
# logo = get_base64_image("frontend/icons/phishing.png")
# img1 = get_base64_image("frontend/icons/txt-file.png")
# img2 = get_base64_image("frontend/icons/monitor.png") 
# img3 = get_base64_image("frontend/icons/performance.png")
# img4 = get_base64_image("frontend/icons/secure.png")
# img5 = get_base64_image("frontend/icons/secure_browse.png")


# # ==============================
# # PAGE CONFIG
# # ==============================
# st.set_page_config(page_title="PhishGuard AI", layout="wide")
# st.markdown("""
# <style>
# .block-container {
#     padding-left: 50px;
#     padding-right: 50px;
# }

# html, body, .main {
#     overflow-x: hidden;
# }
# /* REMOVE DEFAULT TOP SPACE */
# .block-container {
#     padding-top: 0 !important;
# }

# /* HEADER CONTAINER */
# .top-header {
#     position: fixed;
#     top: 0;
#     left: 0;
#     width: 100%;
#     height: 70px;

#     display: flex;
#     align-items: center;
#     justify-content: space-between;

#     padding: 0 40px;

#     background: rgba(2, 12, 27, 0.95);
#     backdrop-filter: blur(10px);

#     z-index: 9999;
#     border-bottom: 1px solid rgba(255,255,255,0.08);
# }

# /* LEFT SIDE (logo + text) */
# .header-left {
#     display: flex;
#     align-items: center;
#     gap: 12px;
# }

# /* TITLE */
# .header-title {
#     font-size: 22px;
#     color: #64ffda;
#     font-weight: 600;
# }

# /* PUSH CONTENT DOWN */
# .main-content {
#     margin-top: 90px;
# }

# /* HOME BUTTON */
# div.stButton > button {

#         background: linear-gradient(
#             135deg,
#             rgba(100,255,218,0.18),
#             rgba(100,255,218,0.08)
#         ) !important;

#         border: 1px solid rgba(100,255,218,0.5) !important;

#         color: #64ffda !important;

#         height: 58px !important;

#         width: 100px !important;

#         border-radius: 14px !important;

#         font-size: 20px !important;

#         font-weight: 600 !important;

#         transition: 0.3s !important;

#         box-shadow:
#         0px 0px 22px rgba(100,255,218,0.15);

#     }

#     div.stButton > button:hover {

#         transform: translateY(-2px);

#         border: 1px solid #64ffda !important;

#         box-shadow:
#         0px 0px 30px rgba(100,255,218,0.35);

#         color: white !important;
#     }

#  /* BUTTON CONTAINER */
# .nav-buttons {
#     position: fixed;
#     top: 18px;   /* ↓ moves buttons slightly down */
#     right: 40px;

#     display: flex;
#     align-items: center;
#     gap: 12px;

#     z-index: 10000;
# }

# /* MAKE STREAMLIT BUTTONS INLINE */
# .nav-buttons div[data-testid="stButton"] {
#     display: inline-block;
# }

# </style>
# """, unsafe_allow_html=True)

# # ==============================
# # REMOVE STREAMLIT UI + PADDING
# # ==============================
# st.markdown("""
# <style>

# /* FULL WIDTH */
# .stApp {
#     margin: 0;
#     padding: 0;
# }

# /* HIDE STREAMLIT */
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# header {visibility: hidden;}

# /* BACKGROUND */
# html, body, .stApp {
#     background:
#         radial-gradient(circle at 20% 20%, #112240, #020c1b),
#         repeating-linear-gradient(
#             0deg,
#             transparent,
#             transparent 1px,
#             rgba(100,255,218,0.05) 1px,
#             rgba(100,255,218,0.05) 2px
#         );
#     color: white;
# }

# /* HERO */
# .hero-container {
#      min-height: 80vh;
#     display: flex;
#     justify-content: space-between;
#     align-items: center;
#     padding: 120px 80px;
# }

# /* TEXT */
# .hero-title {
#     font-size: 64px;
#     font-weight: 800;
#     color: #e6f1ff;
# }

# .hero-sub {
#     margin-top: 20px;
#     font-size: 18px;
#     color: #8892b0;
#     max-width: 500px;
# }

# /* IMAGE */
# .hero-right img {
#     width: 450px;
#     opacity: 0.95;
#     filter: drop-shadow(0px 0px 25px rgba(100,255,218,0.4));
# }

# /* BUTTON */
# .stButton>button {
#     height: 60px;
#     font-size: 18px;
#     border-radius: 12px;
#     background-color: #64ffda;
#     color: black;
#     font-weight: bold;
# }

# /* INPUT */
# .stTextInput>div>div>input,
# .stTextArea textarea {
#     background-color: #112240;
#     color: white;
# }

# /* RESPONSIVE */
# @media (max-width: 900px) {
#     .hero-container {
#         flex-direction: column;
#         text-align: center;
#     }
# }
            
# div.stButton > button {
#     margin-top: 10px;
#     background: #64ffda;
#     border: none;
#     font-size: 20px;
#     color: black;
# }

# div.stButton > button:hover {
#     background: #64ffda;
#     color: black;

# /* HOME BUTTON ONLY */
# .home-btn {
#     #position: fixed;
#     top: 50px;
#     right: 35px;
#     border-radius: 30px;
#     z-index: 10000;
#     background: transparent !important;
# }
# }

# </style>
# """, unsafe_allow_html=True)

# header_col1, header_col2 = st.columns([12,1])

# with header_col1:
#     st.markdown(f"""
#         <div style="
#            display:flex;
#           align-items:center;
#           gap:12px;
#           position:fixed;
#           top:0;
#           left:0;
#           width:100%;
#           height:70px;
#           padding-left:40px;
#           background: rgba(2,12,27,0.95);
#           backdrop-filter: blur(10px);
#           z-index:999;
#           border-bottom:1px solid rgba(255,255,255,0.08);
#         ">
#         <img src="data:image/png;base64,{logo}" width="35">

#         <div style="
#              color:#64ffda;
#              font-size:22px;
#              font-weight:600;
#             ">
#             PhishGuard AI
#         </div>
#         </div>
#     """, unsafe_allow_html=True)

# with header_col2:

#     st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)

#     # HOME BUTTON
#     st.markdown('<div class="home-btn">', unsafe_allow_html=True)

#     if st.button("Home", key="home_btn"):
#         st.session_state.page = "home"
#         st.rerun()

#     st.markdown('</div>', unsafe_allow_html=True)


#     st.markdown('</div>', unsafe_allow_html=True)

#     st.markdown('</div>', unsafe_allow_html=True)

#     st.markdown('</div>', unsafe_allow_html=True)

# # ==============================
# # SESSION STATE
# # ==============================
# if "page" not in st.session_state:
#     st.session_state.page = "home"

# if "input_type" not in st.session_state:
#     st.session_state.input_type = ""

# if "input_data" not in st.session_state:
#     st.session_state.input_data = ""

# # ==============================
# # PAGE 1: LANDING 
# # ==============================

# if st.session_state.page == "home":
#     col1, col2 = st.columns([2, 1])

#     with col1:
#         st.markdown("""
#         <h1 style="font-size:64px; color:#e6f1ff; margin-top: 40px; ">
#         AI-Powered<br>Phishing Detection
#         </h1>
#         """, unsafe_allow_html=True)
        
#         st.markdown("<br><br>", unsafe_allow_html=True)  

#         st.markdown("""
#         <p style="font-size:18px; color:#8892b0; ">
#         Detect malicious emails and URLs in real-time using machine learning and cybersecurity intelligence.<br>
#         PhishGuard AI analyzes emails and URLs using intelligent feature extraction and machine learning models.<br>
#         Get instant results with clear explanations so you understand why something is suspicious.<br>
#         </p>
#         """, unsafe_allow_html=True)

#     with col2:
#         st.image("frontend/icons/hacker.png", width=500)

#     st.markdown("</div>", unsafe_allow_html=True)
#     st.markdown("""
#       <style>
#       img {
#       filter: drop-shadow(0px 0px 30px rgba(100,255,218,0.60));
#       }
#     </style>
#     """, unsafe_allow_html=True)

    

#     st.markdown("""
#      <h2 style="color:#64ffda;">
#       Features
#      </h2>
#      """, unsafe_allow_html=True)


#     col1, col2, col3 = st.columns(3)

#     with col1:
#       st.image("frontend/icons/confidential-email.png", width=60)
#       st.markdown("""
#       <h4 style="color:#ccd6f6";">
#       Email Analysis
#      </h4>
#      """, unsafe_allow_html=True)
            
#       st.markdown("""
#       Analyze email content using AI and cybersecurity rules to identify phishing attempts.  
#       Detects patterns like urgency, suspicious intent, and deceptive messaging techniques used in real-world attacks.
#     """)

#     with col2:
#      st.image("frontend/icons/browsing.png", width=60)
#      st.markdown("""
#       <h4 style="color:#ccd6f6";">
#       URL Analysis 
#      </h4>
#      """, unsafe_allow_html=True)

#      st.markdown(""" 
#      Evaluate URLs for phishing indicators such as suspicious domains, misleading structures, and hidden threats.  
#      Helps identify unsafe links before you click them.
#     """)

#     with col3:
#      st.image("frontend/icons/compliance.png", width=60)
#      st.markdown("""
#       <h4 style="color:#ccd6f6";">
#       Explainable Results  
#      </h4>
#      """, unsafe_allow_html=True)

#      st.markdown(""" 
#      Get instant predictions along with clear reasons behind each decision.  
#      Understand *why* something is flagged as phishing, improving awareness and trust.
#     """)
#     st.markdown("<br><br>", unsafe_allow_html=True)
    
 
#     st.markdown(f"""
#       <h2 style="color:#64ffda;">
#       How It Works
#       </h2>
#     """, unsafe_allow_html=True)

#     st.markdown(f"""
#      <style>
#        .flow-container {{
#         display: flex;
#         align-items: center;
#         justify-content: space-between;
#         margin-top: 30px;
#        }}

#      .flow-box {{
#       background: rgba(100, 255, 218, 0.08);
#       border: 1px solid rgba(100, 255, 218, 0.3);
#       padding: 20px;
#       border-radius: 12px;
#       text-align: left;
#       width: 30%;
#       color: #e6f1ff;
#       backdrop-filter: blur(10px);
#       transition: 0.3s;
#       }}

#      .flow-box:hover {{
#        transform: scale(1.05);
#        box-shadow: 0px 0px 30px rgba(100,255,218,0.4);
#      }}

#      .arrow {{
#       font-size: 28px;
#       color: #64ffda;
#       margin: 0 10px;
#      }}

#      .icon {{
#        margin-bottom: 10px;
#       }}
#      </style>

#      <div class="flow-container">

#     <div class="flow-box">
#      <img src="data:image/png;base64,{img1}" width="50" class="icon">
#      <h4 style="color: #ccd6f6"> Enter Input</h4>
#      <p>
#      Paste an email or URL you want to analyze.<br>
#      The system accepts raw text, links, or suspicious content.<br>
#      Designed for quick and easy user interaction.
#      </p>
#     </div>

#     <div class="arrow">➜</div>

#     <div class="flow-box">
#      <img src="data:image/png;base64,{img2}" width="50" class="icon">
#      <h4 style="color: #ccd6f6"> AI Analysis</h4>
#      <p>
#      The model extracts features like keywords, links, and structure.<br>
#      It analyzes behavioral patterns and phishing indicators.<br>
#      Uses trained ML algorithms to detect threats.
#      </p>
#     </div>

#     <div class="arrow">➜</div>

#     <div class="flow-box">
#      <img src="data:image/png;base64,{img3}" width="50" class="icon">
#      <h4 style="color: #ccd6f6"> Results</h4>
#      <p>
#      Instantly classifies input as safe or phishing.<br>
#      Provides confidence score and risk indicators.<br>
#      Explains the reasoning behind the prediction.
#      </p>
#      </div>

#      </div>
#     """, unsafe_allow_html=True)
#     st.markdown("<br><br>", unsafe_allow_html=True)


#     st.markdown("""
#       <style>
#         .phishing-box {
#         background: rgba(255,255,255,0.04);
#         border: 1px solid rgba(255,255,255,0.06);
#         border-radius: 22px;
#         padding: 35px;
#         margin-top: 20px;
#         margin-bottom: 40px;
#         backdrop-filter: blur(10px);
#        }

#      .stat-card {
#          text-align: center;
#      }

#      .stat-number {
#          font-size: 34px;
#          font-weight: bold;
#          color: #64ffda;
#      }

# .     stat-text {
#     color: #ccd6f6;
#     font-size: 15px;
#     line-height: 1.6;
# }

# .main-text {
#     color: #8892b0;
#     font-size: 17px;
#     line-height: 1.8;
#     margin-top: 10px;
# }

# </style>
# """, unsafe_allow_html=True)

#     st.markdown("""
#     <div class="phishing-box">

#      <h2 style="color:#64ffda; margin-bottom:10px;">
#      Why Phishing Matters
#      </h2>

#      <p class="main-text">
#      Phishing attacks remain one of the most common and dangerous cyber threats       worldwide. 
#      Millions of users fall victim to deceptive emails and malicious links every       year, leading to data theft, financial loss, and security breaches.
#      </p>

#      </div>
#     """, unsafe_allow_html=True)

#     st.markdown("<br>", unsafe_allow_html=True)

#     col1, col2, col3 = st.columns(3)

#     with col1:
#         st.markdown("""
#          <div class="phishing-box">
#          <div class="stat-card">
#          <div class="stat-number">90%</div>
#          <div class="stat-text">
#          of cyberattacks begin with phishing emails
#          </div>
#          </div>
#         """, unsafe_allow_html=True)

#     with col2:
#         st.markdown("""
#          <div class="phishing-box">
#          <div class="stat-card">
#          <div class="stat-number">85%</div>
#          <div class="stat-text">
#          of users click suspicious links without verification
#          </div>
#          </div>
#         """, unsafe_allow_html=True)

#     with col3:
#         st.markdown("""
#          <div class="phishing-box">
#          <div class="stat-card">
#          <div class="stat-number">3.4B</div>
#          <div class="stat-text">
#          phishing emails are sent globally every day
#          </div>
#          </div>       
#         """, unsafe_allow_html=True)
#     st.markdown("<div style='height:50px'></div>", unsafe_allow_html=True)

#     st.markdown("<br><br>", unsafe_allow_html=True)

#     # -----------------------------
#     #  GRAPH SECTION (ADD HERE)
#     # -----------------------------
#     import pandas as pd
#     import matplotlib.pyplot as plt
#     import streamlit as st

#     st.markdown("""
#      <h4 style="color:#64ffda;">
#       Global Phishing Trends
#      </h4>
#     """, unsafe_allow_html=True)

#     st.markdown("""
#      <p style="color:#8892b0;">
#      Based on reports from the Anti-Phishing Working Group (APWG).
#      </p>
#     """, unsafe_allow_html=True)

#     # Data
#     data = {
#        "Year": ["2020", "2021", "2022", "2023", "2024", "2025"],
#        "Attacks": [1.0, 3.2, 4.1, 4.5, 4.8, 3.8]
#     }

#     df = pd.DataFrame(data)

#     # GRAPH (SMALL + CLEAN)
# # -----------------------------
#     fig, ax = plt.subplots(figsize=(4, 2.5))

# # Transparent background
#     fig.patch.set_alpha(0)
#     ax.set_facecolor("none")

# # Bars
#     ax.bar(df["Year"], df["Attacks"])

# # Styling
#     ax.set_title("Phishing Growth", fontsize=10, color="#ccd6f6")
#     ax.set_xlabel("Year", fontsize=8, color="#ccd6f6")
#     ax.set_ylabel("Attacks (M)", fontsize=8, color="#ccd6f6")

#     ax.tick_params(axis='both', labelsize=8, color="#ccd6f6")
#     ax.tick_params(axis='x', colors="#8892b0")
#     ax.tick_params(axis='y', colors="#8892b0")

# # Remove extra borders
#     ax.spines["top"].set_visible(False)
#     ax.spines["right"].set_visible(False)
#     ax.spines["bottom"].set_color("#8892b0")
#     ax.spines["left"].set_color("#8892b0")


#     plt.tight_layout()

# # -----------------------------
# # LAYOUT (LEFT SIDE ONLY)
# # -----------------------------
#     col1, spacer, col2 = st.columns([1, 0.3, 1])

#     with col1:
#      st.pyplot(fig)

#     with col2:
#      st.markdown("""
#         <div style="color:#ccd6f6; line-height:1.8;">
#         <h3 style="color:#64ffda;">Insights</h3>

#         - Phishing attacks have surged globally in recent years, reaching record-breaking         volumes across multiple industries  
#         - According to Anti-Phishing Working Group (APWG) reports, 2024 recorded one of the         highest levels of phishing activity ever observed  
#         - High-value sectors such as financial services, e-commerce, and SaaS platforms         remain primary targets due to sensitive data exposure  
#         - Attack techniques have evolved significantly, incorporating AI-generated emails,         realistic impersonation, and deceptive domain structures  
#         -The increasing scale and sophistication of attacks highlight the urgent need for         automated, intelligence-driven detection systems  
    
#       </div>
#      """, unsafe_allow_html=True)


#     # MORE SPACE BELOW BUTTON
#     st.markdown("<br><br>", unsafe_allow_html=True)

#     # BUTTON CENTER
#     col1, col2, col3 = st.columns([2,0.5,2])

#     with col2:
#         if st.button("Start",  key="start_btn"):
    
#          st.session_state.page = "input"
#          st.rerun()

#     # EXTRA SPACE BELOW BUTTON (you asked this)
#     st.markdown("<br><br>", unsafe_allow_html=True)
#     st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
#     st.markdown("""
#      <div style="
#      margin-top:60px;
#      padding:20px 0;
#      border-top:1px solid rgba(255,255,255,0.1);
#      text-align:center;
#      color:#8892b0;
#      font-size:14px;
#      ">
#       <p style="text-align:center; color:#8892b0;">
#        © 2026 PhishGuard AI • Built with AI + Cybersecurity
#       </p>
#     """, unsafe_allow_html=True)

# # # ==============================
# # # PAGE 2: SELECT TYPE
# # # ==============================

# elif st.session_state.page == "input":

#     # ==============================
#     # PAGE TITLE
#     # ==============================

#     st.markdown("""
#     <h1 style="
#     text-align:center;
#     color:#e6f1ff;
#     font-size:50px;
#     margin-top:1px;
#     margin-bottom:3px;
#     font-weight:800;
#     ">
#     Choose Analysis Type
#     </h1>
#     """, unsafe_allow_html=True)

#     st.markdown("""
#     <p style="
#     text-align:center;
#     color:#8892b0;
#     font-size:22px;
#     margin-bottom:50px;
#     ">
#     Select an option below to start scanning and detecting phishing threats
#     </p>
#     """, unsafe_allow_html=True)

#     # ==============================
#     # CARD CSS
#     # ==============================

#     st.markdown("""
#     <style>

#     .glow-circle {

#         width: 150px;
#         height: 150px;

#         border-radius: 50%;

#         margin: auto;

#         display:flex;
#         align-items:center;
#         justify-content:center;

#         border: 4px solid #64ffda;

#         box-shadow:
#         0px 0px 30px rgba(100,255,218,0.5),
#         0px 0px 60px rgba(100,255,218,0.18);

#         margin-bottom: 30px;
#     }

#     .glow-circle-blue {

#         width: 150px;
#         height: 150px;

#         border-radius: 50%;

#         margin: auto;

#         display:flex;
#         align-items:center;
#         justify-content:center;

#         border: 4px solid #2ea8ff;

#         box-shadow:
#         0px 0px 30px rgba(46,168,255,0.5),
#         0px 0px 60px rgba(46,168,255,0.18);

#         margin-bottom: 30px;
#     }

#     .card-title {

#         color:#e6f1ff;

#         font-size:35px;

#         font-weight:500;

#         margin-top:10px;
#     }

#     .card-desc {

#         color:#8892b0;

#         font-size:20px;

#         line-height:1.9;

#         margin-top:25px;

#         padding-left:15px;
#         padding-right:15px;
#     }

#     </style>
#     """, unsafe_allow_html=True)

#     # ==============================
#     # MAIN SECTION
#     # ==============================

#     left, center, right = st.columns([5,1,5])

#     # ==============================
#     # EMAIL CARD
#     # ==============================

#     with left:

#         st.markdown(f"""
#       <div class="glow-circle">

#         <img src="data:image/png;base64,{img4}"
#         width="105"
#         style="
#         filter:
#         drop-shadow(0px 0px 10px #64ffda)
#         drop-shadow(0px 0px 22px #64ffda);
#         ">

#       </div>
#       """, unsafe_allow_html=True)


#         st.markdown("""
#          <h2 style="
#          color:#e6f1ff;
#          text-align:center;
#          font-size:45px;
#          margin-top:40px;
#          ">
#          Analyze Email
#          </h2>
#         """, unsafe_allow_html=True)

#         st.markdown("""
#          <p style="
#          color:#8892b0;
#          font-size:22px;
#          line-height:2;
#          text-align:center;
#          padding:0px 50px;
#          ">
#          Scan suspicious emails and detect phishing attempts,
#          malicious content, and fake senders using intelligent
#          AI-powered analysis.
#          </p>
#         """, unsafe_allow_html=True)

#         st.markdown("<br><br>", unsafe_allow_html=True)

#         btn_l, btn_c, btn_r = st.columns([1,1,1])

#         with btn_c:
#           if st.button(
#           "Scan",
#           key="email_analysis_final"
#          ):

#             st.session_state.input_type = "Email"
#             st.session_state.page = "analyze"
#             st.rerun()

#         st.markdown("</div>", unsafe_allow_html=True)

#     with center:

#      st.markdown("""
#         <div style="
#         display:flex;
#         flex-direction:column;
#         align-items:center;
#         justify-content:center;
#         height:650px;
#        ">

#         <div style="
#             width:2px;
#             height:160px;
#             background: linear-gradient(
#                 to bottom,
#                 transparent,
#                 #64ffda,
#                 transparent
#             );
#             box-shadow:0px 0px 12px rgba(100,255,218,0.6);
#         ">
#         </div>

#         <div style="
#             width:90px;
#             height:90px;
#             border-radius:50%;
#             border:2px solid #64ffda;
#             display:flex;
#             align-items:center;
#             justify-content:center;
#             color:#64ffda;
#             font-size:32px;
#             font-weight:700;
#             margin:18px 0;
#             background:rgba(10,25,47,0.95);
#             box-shadow:
#             0px 0px 20px rgba(100,255,218,0.35);
#         ">
#         OR
#         </div>

#         <div style="
#             width:2px;
#             height:160px;
#             background: linear-gradient(
#                 to bottom,
#                 transparent,
#                 #64ffda,
#                 transparent
#             );
#             box-shadow:0px 0px 12px rgba(100,255,218,0.6);
#         ">
#         </div>

#       </div>
#       """, unsafe_allow_html=True)
   
#     with right:
#     # ==============================
#     # URL ICON CIRCLE
#     # ==============================

#       st.markdown(f"""
#       <div class="glow-circle-blue">

#         <img src="data:image/png;base64,{img5}"
#         width="105"
#         style="
#         filter:
#         drop-shadow(0px 0px 10px #2ea8ff)
#         drop-shadow(0px 0px 22px #2ea8ff);
#         ">

#       </div>
#       """, unsafe_allow_html=True)

#     # ==============================
#     # TITLE
#     # ==============================

#       st.markdown("""
#       <h2 style="
#       color:#e6f1ff;
#       text-align:center;
#       font-size:45px;
#       margin-top:40px;
#       ">
#       Analyze URL
#       </h2>
#       """, unsafe_allow_html=True)

#     # ==============================
#     # DESCRIPTION
#     # ==============================

#       st.markdown("""
#       <p style="
#       color:#8892b0;
#       font-size:22px;
#       line-height:2;
#       text-align:center;
#       padding:0px 50px;
#       ">
#       Inspect suspicious URLs and websites for phishing risks,
#       malicious redirects, and dangerous domains
#       using smart threat detection.
#       </p>
#       """, unsafe_allow_html=True)

#       st.markdown("<br><br>", unsafe_allow_html=True)


#     # ==============================
#     # BUTTON
#     # ==============================

#       btn_l, btn_c, btn_r = st.columns([1,1,1])

#       with btn_c:
#         if st.button(
#          "Scan",
#          key="url_analysis_final"
#         ):

#          st.session_state.input_type = "URL"
#          st.session_state.page = "analyze"
#          st.rerun()

# # ==============================
# # PAGE 3: INPUT
# # ==============================
# elif st.session_state.page == "analyze":
    
#     input_type = st.session_state.get("input_type", "Email")
#     # ==============================
#     # PAGE STYLING
#     # ==============================

#     st.markdown("""
#     <style>
     
#     html, body {
#      overflow: hidden !important;
#     }

#     .main {
#      overflow: hidden !important;
#     }

#     .block-container {
#      padding-top: 0rem !important;
#      max-width: 100% !important;
#     }
                
#     /* REMOVE STREAMLIT SPACE */
#     .block-container{
#         padding-top: 0rem !important;
#         padding-bottom: 2rem !important;
#         max-width: 100% !important;
#     }

#     /* TEXT AREA */
#     .stTextArea textarea{

#         background: rgba(17,34,64,0.75) !important;

#         color: #e6f1ff !important;

#         border: 1px solid rgba(100,255,218,0.35) !important;

#         border-radius: 18px !important;

#         padding: 20px !important;

#         font-size: 18px !important;

#         min-height: 150px !important;

#         box-shadow:
#         0px 0px 20px rgba(100,255,218,0.08);
                     
#       }
#     </style>
#     """, unsafe_allow_html=True)

 

#     # ==============================
#     # ICON
#     # ==============================

#     icon_path = (
#       "frontend/icons/secure.png"
#       if input_type == "Email"
#       else "frontend/icons/secure_browse.png"
#     )

#     icon_left, icon_center, icon_right = st.columns([3,1,3])

#     with icon_center:

#      st.image(
#         icon_path,
#         width=100
#      )

# # ==============================
# # TITLE
# # ==============================
#     analysis_title = ( 
#        "Analyze Email" if input_type == "Email" 
#         else "Analyze URL"
#     )

#     st.markdown(f"""
#     <h1 style="
#     text-align:center;
#     color:#e6f1ff;
#     font-size:50px;
#     margin-top:0px;
#     margin-bottom:8px;
#     ">
#      {analysis_title}
#     </h1>
#     """, unsafe_allow_html=True)


# # ==============================
# # SUBTITLE
# # ==============================
#     subtitle = (
#      "Paste the email content below and let our AI analyze it<br>"
#      "for phishing threats and suspicious indicators."
#      if input_type == "Email"
#      else
#      "Paste the URL below and let our AI analyze it<br>"
#      "for phishing threats and suspicious indicators."
#     )

#     st.markdown(f"""
#     <p style="
#     text-align:center;
#     color:#8892b0;
#     font-size:24px;
#     line-height:1.5;
#     margin-bottom:10px;
#     ">
#     {subtitle}
#     </p>
#     """, unsafe_allow_html=True)


# # ==============================
# # INPUT AREA
# # ==============================
#     left_space, center_area, right_space = st.columns([1,5,1])

#     with center_area:
      
#       label_text = (
#       "Paste email content here:"
#        if input_type == "Email"
#        else
#       "Paste URL here:"
#       )

#     st.markdown(
#      f"<p style='color:#64ffda;font-size:24px;font-weight:600;margin-bottom:10px;'>{label_text}</p>",
#      unsafe_allow_html=True
#     )

#     email_text = st.text_area(
#         "",
#         height=100,
#         placeholder=(
#         "Paste the full email content here..."
#         if input_type == "Email"
#         else
#         "https://example.com"
#         ),
#         key="email_input_box",
#         label_visibility="collapsed"
#      )
#     # ==============================
#     # SMALL RED WARNING
#     # ==============================

#     if "show_email_warning" not in st.session_state:
#         st.session_state.show_email_warning = False

#     if st.session_state.show_email_warning:
#         warning_text = (
#          "Please enter email text"
#          if input_type == "Email"
#          else
#          "Please enter URL"
#         )

#         st.markdown(f"""
#         <p style="
#         color:#ff6b6b;
#         margin-top:3px;
#         font-size:16px;
#         ">
#         {warning_text}
#         </p>
#         """, unsafe_allow_html=True)


# # ==============================
# # BUTTON
# # ==============================

#     st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

#     btn_left, btn_center, btn_right = st.columns([2,1,2])

#     with btn_center:

#       analyze_clicked = st.button(
#         "Analyze",
#         key="analyze_email_button"
#       )


# # ==============================
# # VALIDATION
# # ==============================

#     if analyze_clicked:

#      if not email_text.strip():

#         st.session_state.show_email_warning = True
#         st.rerun()

#      else:

#         st.session_state.show_email_warning = False

#         # Save input
#         st.session_state.input_data = email_text

#         # Go to result page
#         st.session_state.page = "result"

#         st.rerun()

# elif st.session_state.page == "result":

#     st.markdown("""
#     <style>

#     html, body {
#         overflow:hidden !important;
#     }

#     .block-container{
#         padding-top:0rem;
#         padding-bottom:0rem;
#         max-width:1400px;
#     }

#     .result-card{
#         background: rgba(17,34,64,0.75);
#         border:1px solid rgba(100,255,218,0.15);
#         border-radius:24px;
#         padding:28px;
#         backdrop-filter: blur(12px);
#     }

#     .risk-circle{
#         width:180px;
#         height:180px;
#         border-radius:50%;
#         border:10px solid #ff5a67;

#         display:flex;
#         flex-direction:column;
#         justify-content:center;
#         align-items:center;

#         margin:auto;

#         box-shadow:
#         0px 0px 30px rgba(255,90,103,0.25);
#     }

#     .reason-box{
#         background: rgba(17,34,64,0.55);
#         border-radius:16px;
#         padding:16px;
#         margin-bottom:10px;
#     }

#     </style>
#     """, unsafe_allow_html=True)

#     # API CALL

#     if st.session_state.input_type == "Email":

#         response = requests.post(
#             "http://127.0.0.1:5000/predict-email",
#             json={"text": st.session_state.input_data}
#         )

#     else:

#         response = requests.post(
#             "http://127.0.0.1:5000/predict-url",
#             json={"url": st.session_state.input_data}
#         )

#     data = response.json()

#     # -------------------------
#     # HEADER
#     # -------------------------

#     st.markdown("""
#     <h1 style="
#     text-align:center;
#     color:white;
#     margin-bottom:0px;
#     ">
#     Detection Result
#     </h1>

#     <p style="
#     text-align:center;
#     color:#8892b0;
#     margin-bottom:3px;
#     ">
#     Here's what our AI found.
#     </p>
#     """, unsafe_allow_html=True)

#     # -------------------------
#     # MAIN CARD
#     # -------------------------

#     left,right = st.columns([1,2])

#     with left:

#     #   score = round(float(data.get("confidence", 0)))
#       if st.session_state.input_type == "Email":
#        score = data.get("confidence", 0)
#        score_label = "Confidence"

#       else:
#        score = data.get("risk_score", 0)
#        score_label = "Risk Score"

#       st.markdown(
#         f"""
#         <div style="text-align:center;">

#         <h1 style="
#         color:#64ffda;
#         font-size:50px;
#         margin-bottom:0px;
#         ">
#         {score}%
#         </h1>

#         <p style="
#         color:#8892b0;
#         font-size:18px;
#         margin-top:0px;
#         ">
#         {score_label}
#         </p>

#         </div>
#         """,
#         unsafe_allow_html=True
#       )

    
#     with right:

#      if data["result"] == "Phishing":
#         result_color = "#ff5a67"
#      elif data["result"] == "Safe":
#         result_color = "#0eec37d3"
#      else:
#         result_color = "#f4c508"

#      st.markdown(
#         f"""
#         <div class="result-card">

#         <h2 style="
#         color:{result_color};
#         margin-bottom:0px;
#         ">
#         {data['result']}
#         </h2>

#         <p style="
#         color:#8892b0;
#         font-size:18px;
#         margin-bottom:0px;
#         ">
#         Analysis completed successfully
#         </p>

#         </div>
#         """,
#         unsafe_allow_html=True
#      )

#      colA, colB = st.columns(2)
#      with colA:

#         st.markdown("""
#         <p style="
#         color:#8892b0;
#         margin-bottom:0px;
#         ">
#         Type
#         </p>
#         """, unsafe_allow_html=True)

#         st.markdown(
#             f"""
#             <h2 style="
#             color:#3b82f6;
#             margin-top:0px;
#             ">
#             {st.session_state.input_type}
#             </h2>
#             """,
#             unsafe_allow_html=True
#         )

#      with colB:
      
#       st.markdown("<br>", unsafe_allow_html=True)

#     # -------------------------
#     # REASONS
#     # -------------------------

#     st.markdown("""
#     <h3 style="
#     color:white;
#     margin-bottom:0px;
#     ">
#     Why this result?
#     </h3>
#     """, unsafe_allow_html=True)

#     for reason in data["reasons"][:3]:

#         st.markdown(f"""
#         <div class="reason-box">
#              {reason}
#         </div>
#         """, unsafe_allow_html=True)

#     st.markdown("<br>", unsafe_allow_html=True)

#     # -------------------------
#     # BUTTON
#     # -------------------------

#     c1,c2,c3 = st.columns([2,1,2])

#     with c2:

#         if st.button(
#             "Check Another",
#             use_container_width=True,
#             key="check_again_btn"
#         ):

#             st.session_state.page = "input"
#             st.rerun()

import streamlit as st

from utilities.images import load_all_images
from styles.global_style import apply_global_style
from utilities.header import render_header
from pages.home_page import render_home
from pages.input_page import render_input_page
from pages.analyze_page import render_analyze_page
from pages.result_page import render_result_page


# PAGE CONFIG
st.set_page_config(page_title="PhishGuard AI", layout="wide")


# GLOBAL STYLES + IMAGES
apply_global_style()
images = load_all_images()

# HEADER (shown on every page)
render_header(images["logo"])


# SESSION STATE
if "page" not in st.session_state:
    st.session_state.page = "home"

if "input_type" not in st.session_state:
    st.session_state.input_type = ""

if "input_data" not in st.session_state:
    st.session_state.input_data = ""


# ROUTER
if st.session_state.page == "home":
    render_home(images)

elif st.session_state.page == "analyze":
    render_analyze_page(images)

elif st.session_state.page == "input":
    render_input_page()

elif st.session_state.page == "result":
    render_result_page()
