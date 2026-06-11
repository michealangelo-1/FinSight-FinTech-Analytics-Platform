import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error

# =====================================
# Load Data
# =====================================

df = pd.read_csv("data/raw/aapl_stock_data.csv")

df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

series = df["Close"]

# =====================================
# Train-Test Split
# =====================================

train_size = int(len(series) * 0.8)

train = series[:train_size]
test = series[train_size:]

print(f"Train size: {len(train)}")
print(f"Test size: {len(test)}")

# =====================================
# Train ARIMA Model
# =====================================

model = ARIMA(train, order=(5, 1, 0))
model_fit = model.fit()

# =====================================
# Forecast
# =====================================

predictions = model_fit.forecast(steps=len(test))

# =====================================
# Evaluation Metrics
# =====================================

mae = mean_absolute_error(test, predictions)

rmse = np.sqrt(
    mean_squared_error(test, predictions)
)

print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")

# =====================================
# Save Metrics
# =====================================

metrics_df = pd.DataFrame({
    "Metric": ["MAE", "RMSE"],
    "Value": [mae, rmse]
})

metrics_df.to_csv(
    "outputs/forecasts/forecast_metrics.csv",
    index=False
)

print("Metrics saved.")

# =====================================
# Save Forecast Results
# =====================================

forecast_df = pd.DataFrame({
    "Actual": test.values,
    "Predicted": predictions.values
})

forecast_df.to_csv(
    "outputs/forecasts/forecast_results.csv",
    index=False
)

print("Forecast results saved.")

# =====================================
# Plot Actual vs Predicted
# =====================================

plt.figure(figsize=(12, 6))

plt.plot(
    test.index,
    test,
    label="Actual"
)

plt.plot(
    test.index,
    predictions.values,
    label="Predicted"
)

plt.title("ARIMA Forecast Performance")

plt.xlabel("Date")
plt.ylabel("Stock Price")

plt.legend()
plt.grid(True)

plt.savefig(
    "outputs/charts/actual_vs_predicted.png"
)

plt.show()

print("Chart saved.")