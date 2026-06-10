from flask import Flask, request, jsonify
import pickle
from utils import analyze_url
import re

app = Flask(__name__)

# Loading Email Model & Vectorizer
email_model = pickle.load(open("model/phishing_model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))


# Helper: Convert technical reasons → user-friendly explanations
def simplify_reasons(reasons):
    simple_reasons = []

    for r in reasons:
        if "URL is too long" in r:
            simple_reasons.append("This link is unusually long, which can be used to hide malicious parts.")

        elif "Too many dots" in r:
            simple_reasons.append("The URL has too many dots, which may indicate a fake or complex domain.")

        elif "@" in r:
            simple_reasons.append("This URL contains '@', which can redirect you to a different site.")

        elif "Not using HTTPS" in r:
            simple_reasons.append("This site is not secure (no HTTPS), so your data may not be safe.")

        elif "suspicious word" in r:
            simple_reasons.append("The link contains words like 'login' or 'bank' often used in scams.")

        elif "brand impersonation" in r.lower():
            simple_reasons.append("This URL may be pretending to be a trusted brand.")

        elif "hyphens" in r:
            simple_reasons.append("Too many '-' symbols can indicate a fake or spammy website.")

        elif "IP address" in r:
            simple_reasons.append("The link uses an IP address instead of a proper domain, which is suspicious.")

        elif "shortener" in r:
            simple_reasons.append("This is a shortened link, which can hide the real destination.")

        else:
            simple_reasons.append(r)

    return simple_reasons

from urllib.parse import urlparse

def generate_email_reasons(text):
    text_lower = text.lower()
    detected = []

    # Extract URLs
    urls = re.findall(r'(https?://\S+)', text)

    # 1. ACTION + LINK (Very strong phishing signal)
    action_words = ["review", "verify", "update", "check", "confirm", "access"]
    if urls and any(word in text_lower for word in action_words):
        detected.append(("Requests user action via external link", 3))

    # 2. TIME PRESSURE / CONSEQUENCES
    pressure_patterns = [
        "within", "hours", "immediately", "as soon as possible",
        "may be limited", "may be suspended", "restricted"
    ]
    if any(p in text_lower for p in pressure_patterns):
        detected.append(("Creates urgency or pressure to act quickly", 3))

    # 3. GENERIC / SUSPICIOUS DOMAIN
    if urls:
        for url in urls:
            domain = urlparse(url).netloc.lower()

            # suspicious structure (not real brand, long, hyphenated)
            if "-" in domain or len(domain.split(".")) > 2:
                detected.append((f"Suspicious domain structure ({domain})", 3))

    # 4. REWARD / INCENTIVE SCAM
    reward_patterns = ["reward", "selected", "offer", "bonus", "gift"]
    if any(word in text_lower for word in reward_patterns) and urls:
        detected.append(("Suspicious reward/incentive with link", 3))

    # 5. ACCOUNT / SECURITY PRETEXT
    security_words = ["account", "activity", "login", "transaction", "sign-in"]
    if any(word in text_lower for word in security_words) and urls:
        detected.append(("Pretends to be account/security-related request", 2))

    # 6. ATTACHMENT PHISHING
    if "attachment" in text_lower or ".zip" in text_lower or ".exe" in text_lower:
        detected.append(("Suspicious attachment detected", 3))

    # 7. GENERIC GREETING 
    if re.search(r"\b(dear|hello|hi)\b", text_lower):
        detected.append(("Generic greeting used", 1))

    # 8. LINK ALWAYS A BASE SIGNAL
    if urls:
        detected.append(("Contains external link", 2))

    # SORT by priority
    detected = sorted(detected, key=lambda x: x[1], reverse=True)

    # Remove duplicates
    final = []
    for reason, _ in detected:
        if reason not in final:
            final.append(reason)

    return final[:3] if final else ["Suspicious content detected"]

@app.route("/predict-email", methods=["POST"])
def predict_email():
    data = request.get_json()
    text = data.get("text")

    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    text_vector = vectorizer.transform([text])

    prediction = email_model.predict(text_vector)[0]
    probability = email_model.predict_proba(text_vector)[0][1]

# Extra phishing checks
    text_lower = text.lower()

    rule_score = 0

    if "verify" in text_lower:
      rule_score += 1

    if "password" in text_lower:
      rule_score += 1

    if "account" in text_lower:
      rule_score += 1

    if "urgent" in text_lower:
      rule_score += 1

    if "immediately" in text_lower:
      rule_score += 1

    if "suspended" in text_lower:
      rule_score += 1

    # If many phishing words found,force it to phishing
    if rule_score >= 3:
      prediction = 1
      probability = 0.90

    result = "Phishing" if prediction == 1 else "Safe"
    if result == "Safe":
     reasons = [
        "No suspicious patterns were found in this email.",
        "The email appears safe, but always be cautious with links and attachments."
    ]
    else:
     reasons = generate_email_reasons(text)



    return jsonify({
        "type": "email",
        "input": text,
        "result": result,
        "confidence": round(probability * 100, 2),
        "reasons": reasons
    })



# URL PREDICTION
@app.route("/predict-url", methods=["POST"])
def predict_url():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    result, score, reasons = analyze_url(url)

    # Convert to user-friendly reasons
    if result == "Safe" and not reasons:
     simple_reasons = [
        "No suspicious patterns were detected in this URL.",
        "The link appears safe, but avoid entering sensitive information unless you trust the source."
    ]
    else:
     simple_reasons = simplify_reasons(reasons)

    return jsonify({
        "type": "url",
        "input": url,
        "result": result,
        "risk_score": score,
        "reasons": simple_reasons
    })



# HOME
@app.route("/")
def home():
    return "AI Phishing Detection API Running"


if __name__ == "__main__":
    app.run(debug=True)