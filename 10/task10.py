import pandas as pd

# Data prep
# with open('10/task10_input_test.txt', 'r') as f:
with open('task10_input.txt', 'r') as f:
    input_data = f.read()

input_data = input_data.split('\n')
input_data = input_data[:len(input_data) - 1]
input_data = [i.strip('position=< ') for i in input_data]
input_data = [i.strip('>') for i in input_data]
input_data = [i.replace(' velocity=', '') for i in input_data]
input_data = [i.replace('  ', ' ') for i in input_data]
input_data = [i.replace('><', ',') for i in input_data]
input_data = [i.replace(' ', '') for i in input_data]
input_data = [i.split(',') for i in input_data]

df = pd.DataFrame(input_data, columns=['x', 'y', 'dx', 'dy'])

df['x'] = pd.to_numeric(df['x'], downcast='integer')
df['y'] = pd.to_numeric(df['y'], downcast='integer')
df['dx'] = pd.to_numeric(df['dx'], downcast='integer')
df['dy'] = pd.to_numeric(df['dy'], downcast='integer')


# Find edges for each print
def edges(df):
    desc = df.describe()
    min_x = int(desc['x'].loc['min'])
    max_x = int(desc['x'].loc['max'])
    min_y = int(desc['y'].loc['min'])
    max_y = int(desc['y'].loc['max'])
    return [min_x, max_x, min_y, max_y]


# Update positions
def move(df):
    output = pd.DataFrame()
    output['x'] = df['x'] + df['dx']
    output['y'] = df['y'] + df['dy']
    output['dx'] = df['dx']
    output['dy'] = df['dy']
    return output


def printer(df, edges):
    # Print all dots
    canvas = [['.' for x in range(edges[0], edges[1] + 1)]
              for y in range(edges[2], edges[3] + 1)]
    # Set hashes
    for i, cord in df.iterrows():
        canvas[cord[1] - edges[2]][cord[0] - edges[0]] = '#'
    for i in canvas:
        print(''.join(i))


# When area decreases
decrease = True
seconds = 0
borders = edges(df)
new_size = ((borders[1] - borders[0]) * (borders[3] - borders[2]))
size = new_size + 5
df_new = df

while size > new_size:
    size = new_size
    df_new = move(df)
    borders_new = edges(df_new)
    new_size = ((borders_new[1] - borders_new[0])
                * (borders_new[3] - borders_new[2]))
    if size > new_size:
        seconds += 1
        df = df_new
printer(df, edges(df))
print(seconds)
