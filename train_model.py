import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
from preprocessing import load_data, preprocess

# Load & preprocess
df = load_data("../data/churn_data.csv")
df = preprocess(df)

# Split
X = df.drop("Churn", axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
with open("../model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")