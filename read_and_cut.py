import pandas as pd
from datetime import datetime
import time
import numpy as np

start_read_time = time.time()
custom_date_parser = lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
df = pd.read_csv('database.csv', parse_dates=['departure', 'return'], date_parser=custom_date_parser)

df['year'] = df['departure'].dt.year
df['month'] = df['departure'].dt.month
print('Read time')
print(time.time()-start_read_time)

start_time_np = time.time()

for i in range(2016, 2021):
    for j in range(1,13):
        idx = np.where((df['year'] == i) & (df['month'] == j))
        df.loc[idx].to_csv(f'{i}_{j}_np.csv')


print('Numpy time')
print(time.time()-start_time_np)

