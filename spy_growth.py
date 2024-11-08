import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the stock symbol and period
symbol = "SPY"
start_date = "2023-01-01"
end_date = "2023-12-31"

# Download the stock data
spy_data = yf.download(symbol, start=start_date, end=end_date)

# Calculate percentage growth
spy_data["Pct Change"] = spy_data["Close"].pct_change() * 100
annual_growth = spy_data["Pct Change"].sum()

# Display the result
print(f"The annual percentage growth of SPY for the period from {start_date} to {end_date} is: {annual_growth:.2f}%")

# Plot the percentage change
plt.figure(figsize=(10, 5))
plt.plot(spy_data.index, spy_data["Pct Change"], label='Daily % Change', color='blue')
plt.xlabel('Date')
plt.ylabel('Daily Percentage Change (%)')
plt.title('SPY Daily Percentage Growth (2023)')
plt.legend()
plt.grid()

# Save the chart as an image in the current directory
plt.savefig('spy_growth_chart.png')
print("Chart saved as 'spy_growth_chart.png'")
