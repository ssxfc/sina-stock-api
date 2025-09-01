import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import mplfinance as mpf
from sklearn.preprocessing import MinMaxScaler
import torch
import torch.nn as nn
import time
import math
from sklearn.metrics import mean_squared_error

# 导入数据
filepath = 'stock_data.csv'
df = pd.read_csv(
    'stock_data.csv',
    parse_dates=['trade_date'],
    index_col='trade_date'
)
df = df.rename(columns={
    'vol': 'volume'
})
df = df.sort_index(ascending=True)
mpf.plot(df, type='line')

# 选取Close作为特征
price = df[['close']]
# 进行归一化操作
scaler = MinMaxScaler(feature_range=(-1, 1))
price['close'] = scaler.fit_transform(price['close'].values.reshape(-1, 1))


# 数据集划分
def split_data(stock, lookback):
    data_raw = stock.to_numpy()
    data = []

    for index in range(len(data_raw) - lookback):
        data.append(data_raw[index: index + lookback])

    data = np.array(data)

    test_set_size = int(np.round(0.2 * data.shape[0]))
    train_set_size = data.shape[0] - (test_set_size)

    x_train = data[:train_set_size, :-1, :]
    y_train = data[:train_set_size, -1, :]
    x_test = data[train_set_size:, :-1, :]
    y_test = data[train_set_size:, -1, :]

    return [x_train, y_train, x_test, y_test]

lookback = 20
x_train, y_train, x_test, y_test = split_data(price, lookback)

class LSTM(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_layers, output_dim):
        super(LSTM, self).__init__()
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_dim).requires_grad_()
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_dim).requires_grad_()
        out, (hn, cn) = self.lstm(x, (h0.detach(), c0.detach()))
        out = self.fc(out[:, -1, :])
        return out

model = LSTM(input_dim=19, hidden_dim=hidden_dim, output_dim=output_dim, num_layers=num_layers)



criterion = torch.nn.MSELoss()
optimiser = torch.optim.Adam(model.parameters(), lr=0.01)

hist = np.zeros(num_epochs)
start_time = time.time()

for t in range(num_epochs):
    y_train_pred = model(x_train)
    loss = criterion(y_train_pred, y_train)
    print("Epoch ", t, "MSE: ", loss.item())
    hist[t] = loss.item()
    optimiser.zero_grad()
    loss.backward()
    optimiser.step()

training_time = time.time() - start_time
print("Training time: {}".format(training_time))

