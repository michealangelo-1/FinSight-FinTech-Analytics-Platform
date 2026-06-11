import yfinance as yf

df = yf.download(
    "AAPL",
    start="2020-01-01",
    end="2025-01-01",
    auto_adjust=True
)

# Remove ticker level if present
df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

df.reset_index(inplace=True)

df.to_csv(
    "data/raw/aapl_stock_data.csv",
    index=False
)

print(df.head())