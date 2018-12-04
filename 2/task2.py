import pandas as pd
from collections import Counter

df = pd.read_csv('task2_input.csv', names=['Strings'])

times = {'doubles': 0, 'triples': 0}

for line in df['Strings']:
    two = False
    three = False
    c = dict(Counter(line))
    # print(c)
    for l, count in c.items():
        if count == 3:
            three = True
        if count == 2:
            two = True
    if two:
        times['doubles'] = times['doubles'] + 1
    if three:
        times['triples'] = times['triples'] + 1

print(times)
print(times['doubles'] * times['triples'])
