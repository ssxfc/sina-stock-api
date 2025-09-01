import mplfinance as mpf
import pandas as pd


df = pd.read_csv(
    'stock_data.csv',
    parse_dates=['trade_date'],
    index_col='trade_date'
)
df = df.rename(columns={
    'vol': 'volume'
})
df = df.sort_index(ascending=True)

# mpf.plot(df, type='line')
# mpf.plot(df, type='line',mav=(5,10,20,30))
# mpf.plot(df, type='line',mav=(5,10,30), volume=True)
# mpf.plot(df.tail(40), type='candle', mav=(3,6,9), volume=True)
mpf.plot(df.tail(40), type='candle', mav=(3,6,9), show_nontrading=True, volume=True)
