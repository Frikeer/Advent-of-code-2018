import pandas as pd
import numpy as np
import re

df = pd.read_csv('task4_input.csv', names=['raw'])

df['time'], df['event'] = df['raw'].str.split(']', 1).str
df['time'] = df['time'].str.lstrip('[')
df['time'] = pd.to_datetime(df['time'])
df.drop('raw', axis=1, inplace=True)

# df['minutes_sleeping'] = np.zeros((1056, 60))
df = df.sort_values(['time', 'event'])

df['ID'] = 0

r = re.compile(r'(?<=#)[0-9]*')
guard = 0

for index, info in df.iterrows():
    match = r.search(info['event'])
    if match == None:
        df.loc[index, 'ID'] = guard
    else:
        guard = match.group()
        df.loc[index, 'ID'] = guard
# Map minutes asleep and put it on the fallin asleep row

df['sleeping_time'] = 0
df = df.reset_index()
df.drop('index', axis=1, inplace=True)
#
for index, info in df.iterrows():
    if info['event'] == ' falls asleep':
        sleeping_time = (
            (df.loc[index + 1, 'time'] - info['time']).seconds) / 60
        df.loc[index, 'sleeping_time'] = sleeping_time

# Find guard (#283 sleeps the most)

list_ID = df.ID.unique()
# print(list_ID)

df_sleeping = df.loc[(df['event'] == ' falls asleep')].drop(
    'event', axis=1)

results = {}

schedule = np.zeros((60, 1))
for ID in list_ID:
    schedule = np.zeros((60, 1))
    df_ID = df_sleeping[(df_sleeping['ID'] == ID)]
    for index, row in df_ID.iterrows():
        start = row['time'].minute
        stop = start + int(row['sleeping_time'])
        schedule[start:stop] += 1
    results[ID] = schedule
# print(results['283'])


max_value = 0
for key in results:
    if np.amax(results[key]) > max_value:
        max_value = np.amax(results[key])
        max_minute = np.argmax(results[key])
        max_ID = key
        print(max_ID)
        print(max_minute)
        print('\n')
