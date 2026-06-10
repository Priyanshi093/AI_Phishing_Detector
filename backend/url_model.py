import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Ensuring model folder exists
os.makedirs("model", exist_ok=True)

# Loading dataset
df = pd.read_csv("../data/dataset.csv")

print("URL dataset loaded:", df.shape)


# Label conversion
df["Result"] = df["Result"].map({1: 0, -1: 1})

# Features and labels
X = df.drop("Result", axis=1)
y = df["Result"]


# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

print("URL model trained")


# Save model
with open("model/url_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("URL model saved!")