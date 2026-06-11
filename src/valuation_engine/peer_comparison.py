import pandas as pd

from data_loader import get_stock_info


def compare_peers():

    tickers = [
        "AAPL",
        "MSFT",
        "GOOGL",
        "AMZN",
        "TSLA"
    ]

    rows = []

    for ticker in tickers:

        stock = get_stock_info(ticker)

        rows.append({
            "ticker": stock["ticker"],
            "company_name": stock["company_name"],
            "pe_ratio": stock["pe_ratio"],
            "pb_ratio": stock["pb_ratio"],
            "market_cap": stock["market_cap"]
        })

    return pd.DataFrame(rows)
