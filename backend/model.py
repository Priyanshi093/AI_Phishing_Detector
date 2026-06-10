import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os


# Ensuring if model folder exists
os.makedirs("model", exist_ok=True)

# Loading dataset
df = pd.read_csv("../data/CEAS_08.csv")

print("Dataset loaded successfully")
print("Dataset shape:", df.shape)


# Data Cleaning : Remove rows with missing values
df = df.dropna(subset=["subject", "body", "label"])

# Shuffle dataset
df = df.sample(frac=1).reset_index(drop=True)

print("Data cleaned")
print("Remaining rows:", len(df))


# Feature Engineering : Combine subject + body into one text
df["text"] = df["subject"] + " " + df["body"]

# X = df["text"]
# y = df["label"]
X = df["text"]
y = df["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Text Vectorization
vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

X_train_vectorized = vectorizer.fit_transform(X_train)

X_test_vectorized = vectorizer.transform(X_test)

print("Text vectorization complete")
print("Feature shape:", X_train_vectorized.shape)


# Train Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vectorized, y_train)

print("Model trained successfully")

# Model Evaluation
y_pred = model.predict(X_test_vectorized)

accuracy = accuracy_score(y_test, y_pred)

print("\n======================")
print("MODEL EVALUATION")
print("======================")
print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# Save Model & Vectorizer
with open("model/phishing_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("model/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print(" Model and vectorizer saved in /backend/model/")