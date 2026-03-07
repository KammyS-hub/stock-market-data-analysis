import yfinance as yf

# Download stock data
data = yf.download("AAPL", start="2023-01-01", end="2024-01-01")

print(data.head())
import matplotlib.pyplot as plt

# Plot closing price
data['Close'].plot(title="Apple Stock Closing Prices")

plt.xlabel("Date")
plt.ylabel("Price")
plt.show()
