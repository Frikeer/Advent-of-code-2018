import pandas as pd

# Really like pandas for all types of seperate input
df = pd.read_csv('task1_input.csv', names=['Number'])

# Task A
print("Sum of numbers: ")
print(df['Number'].sum())

# Task B
nbr = 0  # The current freq
frequencies = [0]  # List of all resulting freqs
result = 0
stop = False  # Stops outer loop

# Loop through all frequencies and restart. For each frequency added, check if
# it has been previously added
for i in range(0, 250):
    for k in df.Number:
        nbr = nbr + k
        frequencies.append(nbr)
        if frequencies.count(nbr) > 1:  # If freq revisited, will appear twice
            result = nbr
            stop = True
            break
    if stop:
        break
print("First revisited frequency: ")
print(result)
# print(frequencies)
