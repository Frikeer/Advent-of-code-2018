import pandas as pd
from collections import Counter

df = pd.read_csv('task2_input.csv', names=['Strings'])

times = {2: 0, 3: 0}

for line in df:
    letter_count = {}
    Counter
