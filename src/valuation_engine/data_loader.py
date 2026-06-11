import yfinance as yf
import pandas as pd


def get_stock_info(ticker):
    stock = yf.Ticker(ticker)

    return {
        "ticker": ticker,
        "company_name": stock.info.get("longName"),
        "market_cap": stock.info.get("marketCap"),
        "pe_ratio": stock.info.get("trailingPE"),
        "pb_ratio": stock.info.get("priceToBook"),
        "current_price": stock.info.get("currentPrice")
    }
