import yfinance as yf

def getStock(ticker):
    gme = yf.Ticker(ticker)
    # print(gme.info['regularMarketPrice'])
    data = gme.history()
    last_quote = (data.tail(1)['Close'].iloc[0])
    return last_quote

