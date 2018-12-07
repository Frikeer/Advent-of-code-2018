from pathlib import Path
import re

input = Path('task5_input.txt').read_text()

changes = 1

while changes > 0:
    changes = 0
    print(len(input))
    for i in range(0, len(input) - 1):
        if i < len(input) - 1:
            if input[i].isupper() and input[i + 1].islower():
                if input[i] == input[i + 1].capitalize():
                    newstring = input[:i] + input[i + 2:]
                    input = newstring
                    changes += 1
            if input[i].islower() and input[i + 1].isupper():
                if input[i].capitalize() == input[i + 1]:
                    newstring = input[:i] + input[i + 2:]
                    input = newstring
                    changes += 1


# # For testing purposes
# with open('result.txt', 'w') as the_file:
#     the_file.write(input)
