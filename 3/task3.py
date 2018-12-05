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
