import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from tqdm import tqdm

ts1 = pd.read_csv('data/MARA.csv')
ts2 = pd.read_csv('data/RIOT.csv')

ts1_close = np.array(ts1['Close'].tolist())
ts2_close = np.array(ts2['Close'].tolist())

print(ts1_close)
print('-----------------')
print(ts2_close)

num_steps = 300
num_tests = 200

correls_all_ts = []
num_lags = 10
lags = [*range(1,num_lags)]

for lag in tqdm(lags):
    correls = []
    for i in range(num_steps):
        ts1_close_adj = ts1_close[i : i + num_steps]
        ts2_close_adj = ts2_close[i + lag: i + num_steps + lag]
        corr = stats.pearsonr(ts1_close_adj, ts2_close_adj).statistic
        correls.append(corr)
    correls_all_ts.append(np.array(correls).mean())
    
#print(correls_all_ts)

plt.plot(lags, correls_all_ts)
plt.savefig('plot.png')
