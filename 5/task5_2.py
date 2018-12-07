from pathlib import Path
import re

ORG_INPUT = Path('task5_input.txt').read_text()

results = {}
changes = 1
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for a in range(0, len(alphabet)):
    # Remove polymers
    input = ORG_INPUT
    input = input.replace(ALPHABET[a], '')
    input = input.replace(alphabet[a], '')
    print(len(ORG_INPUT))
    changes = 1
    while changes > 0:
        changes = 0
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
    print(a)
    results[a] = len(input)

print(results)

# # For testing purposes
# with open('result.txt', 'w') as the_file:
#     the_file.write(input)
