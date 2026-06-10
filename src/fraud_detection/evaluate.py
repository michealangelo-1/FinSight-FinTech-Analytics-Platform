import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import roc_curve, auc

df = pd.read_csv("data/creditcard.csv")

X = df.drop("Class", axis=1)
y =  df["Class"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model= joblib.load("models/fraud_detection_model.pkl")

y_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm
)

disp.plot()

plt.title("Fraud Detection Confusion Matrix")

plt.savefig(
    "outputs/confusion_matrix.png",
    bbox_inches="tight"
)

y_prob = model.predict_proba(X_test)[:, 1]

fpr, tpr, _ = roc_curve(y_test, y_prob)

roc_auc = auc(fpr, tpr)

plt.figure(figsize=(8,6))
plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.4f}")
plt.plot([0,1], [0,1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend


plt.savefig(
    "outputs/roc_curve.png",
    bbox_inches="tight"
)


importances = model.feature_importances_

indices = np.argsort(importances)[::-1][:10]

plt.figure(figsize=(10,6))

plt.bar(
    range(len(indices)),
    importances[indices]
)

plt.xticks(
    range(len(indices)),
    X.columns[indices],
    rotation=45
)

plt.title("Top 10 Feature Importances")

plt.tight_layout()

plt.savefig(
    "outputs/feature_importance.png",
    bbox_inches="tight"
)

plt.show()