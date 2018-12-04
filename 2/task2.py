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

# print(times)
# print(times['doubles'] * times['triples'])

# Task 2.2
# Ta en rad, ta bort första bokstaven och kolla om den matchar med någon annan
# rad utan första, iterera


# def findEqualString(str, targets):
#     for t in targets:
#         if str == t:
#             return str
#         else:
#             return ''

# Takes string 'line' and index 'i' and returns the same string without
# the letter at index
def stringReduction(line, i):
    if i == 0:
        shortline = line[1:]
    elif i == (len(line)):
        shortline = line[:len(line) - 1]
    else:
        shortline = line[:i] + line[i + 1:]
    return shortline


counter = 0
for line in df['Strings']:  # Examine every string in the series
    for i in range(0, len(line)):  # Create a string minus the letter at index i
        shortline = stringReduction(line, i)
        # Compare with all strings below in series
        for k in range(counter + 1, len(df['Strings'])):
            if shortline == stringReduction(df['Strings'][k], i):
                print(shortline)
    counter = counter + 1
