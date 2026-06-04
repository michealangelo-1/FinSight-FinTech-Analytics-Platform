import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv("data/credit_risk.csv")

df.columns = df.columns.str.strip()

X = df.drop(["loan_id", "loan_status"], axis=1)

X = pd.get_dummies(X, drop_first=True)

y = df["loan_status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y,
    test_size=0.2, 
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

with open("models/credit_risk_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully.")    