import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/raw/aapl_stock_data.csv"
)

df["Date"] = pd.to_datetime(df["Date"])

df.set_index(
    "Date",
    inplace=True
)

# =====================================
# Closing Price Chart
# =====================================

plt.figure(figsize=(12, 6))

plt.plot(df["Close"])

plt.title("Apple Stock Closing Price")

plt.xlabel("Date")
plt.ylabel("Price (USD)")

plt.grid(True)

plt.savefig(
    "outputs/charts/aapl_closing_price.png"
)

plt.show()

# =====================================
# Moving Averages
# =====================================

df["MA_30"] = (
    df["Close"]
    .rolling(window=30)
    .mean()
)

df["MA_100"] = (
    df["Close"]
    .rolling(window=100)
    .mean()
)

plt.figure(figsize=(12, 6))

plt.plot(
    df["Close"],
    label="Close Price"
)

plt.plot(
    df["MA_30"],
    label="30-Day MA"
)

plt.plot(
    df["MA_100"],
    label="100-Day MA"
)

plt.title(
    "Apple Stock Price with Moving Averages"
)

plt.xlabel("Date")
plt.ylabel("Price")

plt.legend()

plt.grid(True)

plt.savefig(
    "outputs/charts/moving_averages.png"
)

plt.show()

print("Charts saved successfully.")