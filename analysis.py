import yfinance as yf
import matplotlib.pyplot as plt

# Ask user for stock ticker
ticker = input("Enter stock ticker: ")

# Download stock data
data = yf.download(ticker, start="2023-01-01", end="2024-01-01")

# Show preview of important columns
print("\nStock Data Preview:")
print(data[['Open', 'High', 'Low', 'Close', 'Volume']].head())

# Plot closing price
data['Close'].plot(title=f"{ticker} Stock Closing Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()

# Calculate 20-day moving average
data['MA20'] = data['Close'].rolling(window=20).mean()

# Plot price and moving average
data[['Close', 'MA20']].plot(title=f"{ticker} Stock Price with 20-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()
