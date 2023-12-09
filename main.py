import numpy as np
import pandas as pd

ts1 = pd.read_csv('data/MARA.csv')
ts2 = pd.read_csv('data/RIOT.csv')

ts1_close = np.array(ts1['Close'].tolist())
ts2_close = np.array(ts2['Close'].tolist())

print(ts1_close)
print('-----------------')
print(ts2_close)
