# AI-Powered Phishing Detector - PhishGuard AI
<img width="1821" height="864" alt="phishing_banner" src="https://github.com/user-attachments/assets/27211ea1-c268-44c6-9e37-6cfd46dc9965" />

## Overview
PhishGuard AI is a machine learning-based web application designed to identify phishing threats in emails and URLs. The system helps users detect malicious content by analyzing email text and website URLs using trained machine learning models.
The application provides a modern and interactive user interface, enabling users to quickly determine whether an email or URL is safe or potentially harmful.

## Features
### Email Phishing Detection
- Detects phishing emails using NLP techniques.
- Uses TF-IDF vectorization for feature extraction.
- Classifies emails as Safe or Phishing.

### URL Phishing Detection
- Analyzes URLs for phishing indicators and suspicious patterns.
- Classifies URLs as Safe or Phishing using Machine Learning.
- Detects potentially malicious websites in real time.
- Provides instant prediction results.

### Machine Learning Powered
- Trained on real-world phishing datasets.
- Utilizes TF-IDF and Logistic Regression models.
- Stores pre-trained models using Pickle.
- Fast and lightweight deployment.

### Interactive Dashboard
- Responsive Streamlit-based UI.
- Easy navigation and analysis workflow.
- Clear visualization of prediction results.

### Real-Time Detection
- Instant email and URL analysis.
- Rapid phishing classification.
- Optimized for minimal processing delay.

## Demo Video
Watch PhishGuard AI in action and see how it detects phishing emails and malicious URLs in real time.
https://github.com/user-attachments/assets/7fb5750b-b103-43fe-8eae-2a0d975c1a79

## Application Screenshots
### Home Page
The landing page introduces the platform and provides users with quick access to phishing detection features.
<img width="1837" height="915" alt="Screenshot 2026-06-06 233955" src="https://github.com/user-attachments/assets/cdacb59d-7e39-4b48-85cd-a0ea881008c6" />
<img width="1824" height="581" alt="Screenshot 2026-06-06 234029" src="https://github.com/user-attachments/assets/8e8524e9-034e-4c7a-95c6-6c410e96c970" />
<img width="1823" height="644" alt="Screenshot 2026-06-06 234100" src="https://github.com/user-attachments/assets/abbf8dca-6b2c-425a-b13e-f6f955056a93" />
<img width="1825" height="893" alt="Screenshot 2026-06-06 234124" src="https://github.com/user-attachments/assets/b9f29984-a7ce-4ec4-abaa-bc9797b85f32" />
<img width="1831" height="921" alt="Screenshot 2026-06-06 234151" src="https://github.com/user-attachments/assets/b74e4c1c-b762-4679-985c-3cb07ab9db9b" />


### Select Page - Email or URL
Users can select whether they want to analyze email or url.
<img width="1832" height="933" alt="Screenshot 2026-06-06 234339" src="https://github.com/user-attachments/assets/d313c6af-45f6-4d9b-a216-933deedd0c83" />
<img width="1829" height="925" alt="Screenshot 2026-06-06 234406" src="https://github.com/user-attachments/assets/1d8fca39-4c13-43de-872c-400bda469d12" />


### Email Phishing Analysis
Users can submit email content for analysis. The system processes the text using NLP techniques and predicts whether the email is legitimate or phishing
<img width="1825" height="935" alt="Screenshot 2026-06-06 234457" src="https://github.com/user-attachments/assets/fb5936b5-7a98-4096-9add-44ec79af5889" />


### URL Phishing Analysis
Users can enter a URL to determine whether it is safe or potentially malicious based on machine learning predictions.
<img width="1830" height="927" alt="Screenshot 2026-06-06 235612" src="https://github.com/user-attachments/assets/9e5206cb-2972-4d12-8a56-e88617b4bc9f" />


### Prediction Results
The results page displays the classification outcome along with relevant threat insights and recommendations.
<img width="1837" height="936" alt="Screenshot 2026-06-06 235251" src="https://github.com/user-attachments/assets/640fc72c-9f53-4131-a51d-fce36e9b71e0" />
<img width="1822" height="933" alt="Screenshot 2026-06-06 235450" src="https://github.com/user-attachments/assets/7b694d07-1777-4b78-a772-476e5c608ad3" />

### Architecture Overview
PhishGuard AI is built on a modular architecture consisting of a Streamlit-based user interface, a Flask-powered backend, a machine learning inference engine for email analysis, and a rule-based URL threat detection module. Incoming emails and URLs are analyzed through specialized security pipelines that identify phishing indicators, assess risk levels, and deliver real-time, explainable threat intelligence to help users make informed security decisions.
<div align="center">
<img src="https://github.com/user-attachments/assets/fdab1172-296e-4d17-9991-28751351393a" width="650"/>
</div>

## Technology Stack
### Frontend
-Streamlit
-HTML
-CSS

### Backend
-Flask
-Python

### Machine Learning
-Scikit-learn
-TF-IDF Vectorizer
-Logistic Regression

### Data Processing
* Pandas
* NumPy

### URL Threat Analysis
-RapidFuzz
-Regular Expressions (Regex)
-urllib.parse

### Development Tools
-Git
-GitHub
-VS Code






