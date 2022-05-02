import yfinance as yf

ticker = yf.Ticker("SHOP")

print(ticker.info)