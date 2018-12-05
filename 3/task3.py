import numpy as np
import pandas as pd

# Getting a nice dataframe
df = pd.read_csv('task3_input.csv', names=['@', 'loc', 'measures'],
                 index_col=0, delim_whitespace=True)
df.drop(['@'], axis=1, inplace=True)

df['x'], df['y'] = df['loc'].str.split(',', 1).str  # Split coordinates
df['y'] = df['y'].str.rstrip(':')  # Remove ':'
df.drop(['loc'], axis=1, inplace=True)  # Drop old concatenated column

df['width'], df['length'] = df['measures'].str.split('x', 1).str
df.drop(['measures'], axis=1, inplace=True)

# Make them numeric
df.x = pd.to_numeric(df.x, errors='raise')
df.y = pd.to_numeric(df.y, errors='raise')
df.width = pd.to_numeric(df.width, errors='raise')
df.length = pd.to_numeric(df.length, errors='raise')

print(df.describe())

# Create canvas, I checked the max values and they are within 1000x1000
canvas = np.zeros((1000, 1000))

# Add 1 for every claim  on the canvas


def marker(x, y, width, length):
    for i in range(x, x + width):
        for j in range(y, y + length):
            canvas[i][j] += 1


# Put all rows through the function
for index, patch in df.iterrows():
    marker(patch['x'], patch['y'], patch['width'], patch['length'])
# Print sum of areas where the claims are more than 1
print((canvas > 1).sum())


def finder(index, x, y, width, length):
    clear = True
    for i in range(x, x + width):
        for j in range(y, y + length):
            if canvas[i][j] > 1:
                clear = False
                break
    if clear:
        print(index)


for index, patch in df.iterrows():
    finder(index, patch['x'], patch['y'], patch['width'], patch['length'])
