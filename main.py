import yfinance as yf
import plotly.graph_objs as go 


stock_name = 'AD.AS'
T = '1d'
delta_t = '2m'

data = yf.download(tickers=stock_name, period=T, interval=delta_t)
data.head()
print(data.head())

fig = go.Figure()
fig.add_trace(go.Candlestick(
    x =data.index,
    open =data['Open'],
    high = data['High'],
    low = data['Low'],
    close = data['Close'],
    name ='Market data'
    
))
fig.show()