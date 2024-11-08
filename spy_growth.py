import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

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

# Plot the percentage change with different colors for positive and negative values
fig = go.Figure()

# Add positive percentage change in green
fig.add_trace(go.Scatter(
    x=spy_data.index,
    y=spy_data["Pct Change"].where(spy_data["Pct Change"] >= 0),
    mode='lines+markers',
    name='Positive Change',
    line=dict(color='green'),
    connectgaps=True
))

# Add negative percentage change in red
fig.add_trace(go.Scatter(
    x=spy_data.index,
    y=spy_data["Pct Change"].where(spy_data["Pct Change"] < 0),
    mode='lines+markers',
    name='Negative Change',
    line=dict(color='red'),
    connectgaps=True
))

# Update layout for better presentation
fig.update_layout(
    title='SPY Daily Percentage Growth (2023)',
    xaxis_title='Date',
    yaxis_title='Daily Percentage Change (%)',
    template='plotly_dark',
    hovermode='x unified'
)

# Show the interactive chart
fig.show()

# Plot the bar chart for positive and negative percentage changes
fig_bar = go.Figure()

# Add positive percentage change bars in green
fig_bar.add_trace(go.Bar(
    x=spy_data.index,
    y=spy_data["Pct Change"].where(spy_data["Pct Change"] >= 0),
    name='Positive Change',
    marker=dict(color='green')
))

# Add negative percentage change bars in red
fig_bar.add_trace(go.Bar(
    x=spy_data.index,
    y=spy_data["Pct Change"].where(spy_data["Pct Change"] < 0),
    name='Negative Change',
    marker=dict(color='red')
))

# Update layout for better presentation
fig_bar.update_layout(
    title='SPY Daily Percentage Growth (2023) - Bar Chart',
    xaxis_title='Date',
    yaxis_title='Daily Percentage Change (%)',
    template='plotly_dark',
    barmode='relative'
)

# Show the bar c