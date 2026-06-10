import re
from urllib.parse import urlparse
from rapidfuzz import fuzz

def analyze_url(url):
    reasons = []
    score = 0

    url_lower = url.lower()

    # Length check
    if len(url) > 75:
        reasons.append("URL is too long")
        score += 1

    # Too many dots
    if url.count(".") > 3:
        reasons.append("Too many dots in URL")
        score += 1

    # @ symbol
    if "@" in url:
        reasons.append("Contains @ symbol")
        score += 2

    # HTTP instead of HTTPS
    if not url_lower.startswith("https"):
        reasons.append("Not using HTTPS")
        score += 1

    # Suspicious keywords
    suspicious_words = ["login",
    "verify",
    "bank",
    "secure",
    "security",
    "account",
    "update",
    "signin",
    "password",
    "wallet",
    "payment"]
    for word in suspicious_words:
        if word in url_lower:
            reasons.append(f"Contains suspicious word: {word}")
            score += 3
            break

    # Extract domain
    domain = urlparse(url).netloc

    # URL shortener detection
    shorteners = [
        "bit.ly", "tinyurl.com", "t.co", "goo.gl",
        "ow.ly", "buff.ly", "adf.ly", "bit.do"
    ]

    if any(short in domain for short in shorteners):
        reasons.append("Uses URL shortener (possible obfuscation)")
        score += 3

    # Brand Impersonation Detection
    brands = [
    "google",
    "paypal",
    "amazon",
    "facebook",
    "microsoft",
    "apple",
    "instagram",
    "netflix"
    ]

#Extract domain name for brand comparison
    domain_name = domain.replace("www.", "")
    domain_name = domain_name.split(".")[0]

# Normalize common phishing substitutions
    normalized_domain = (
     domain_name
     .replace("0", "o")
     .replace("1", "l")
     .replace("3", "e")
     .replace("5", "s")
     .replace("rn", "m")
    )

    for brand in brands:

        similarity = fuzz.ratio(
         normalized_domain,
         brand
        )

    # DEBUG 
        print(
        f"Domain: {normalized_domain} | "
        f"Brand: {brand} | "
        f"Similarity: {similarity}"
        )

        if similarity >= 75 and domain_name != brand:

            reasons.append(
             f"Possible brand impersonation detected ({brand})"
            )

            score += 6
            break


    # Too many hyphens
    if url.count("-") >= 2:
        reasons.append("Too many hyphens in URL")
        score += 2

    # IP address detection
    if re.match(r'\d+\.\d+\.\d+\.\d+', domain):
        reasons.append("Uses IP address instead of domain")
        score += 2

    # Final decision
    if score >= 5:
        result = "Phishing"
    elif score >= 4:
        result = "Suspicious"
    else:
        result = "Safe"

    # Convert score to percentage
    max_score = 18
    risk_percentage = round((score / max_score) * 100)

    #  Adjust ranges for better UI
    if result == "Safe":
      risk_percentage = min(max(risk_percentage, 10), 35)

    elif result == "Suspicious":
      risk_percentage = min(max(risk_percentage, 45), 75)

    else:  # Phishing
      risk_percentage = min(max(risk_percentage, 80), 100)
    
    return result, risk_percentage, reasons