import tushare as ts


ts.set_token('36eddaca658468972c66f70f827d00adcfa9a333b2f346839745b99a')

pro = ts.pro_api()

df = pro.daily(ts_code='000001.SZ', start_date='20200122', end_date='20250827')


df.to_csv('stock_data.csv', index=False, encoding='utf-8')