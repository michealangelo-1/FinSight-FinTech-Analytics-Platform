import pandas as pd 
import joblib

model = joblib.load(
    "models/fraud_detection_model.pkl"
)

df = pd.read_csv("data/creditcard.csv")

sample = df.drop("Class", axis=1).iloc[[0]]

prediction = model.predict(sample)

print("Prediction:", prediction[0])