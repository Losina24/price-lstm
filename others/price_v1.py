import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from datetime import datetime

df = pd.read_csv('AAPL.csv')
close_prices = df['close']
dates = df['date'].map(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S%z'))

plt.plot(dates, close_prices)
plt.title('Apple Stock Price')
plt.xlabel('Date')
plt.xticks(dates[::300], rotation=10)
plt.ylabel('Price')
plt.show()

# LSTM are sensitive to the scale of the data. So we apply MinMax scaler
scaler = MinMaxScaler(feature_range=(0, 1))
datafeed = scaler.fit_transform(np.array(close_prices).reshape(-1, 1))

plt.plot(dates, datafeed)
plt.title('Processed Apple Stock Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
