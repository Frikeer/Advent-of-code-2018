import sys
sys.getrecursionlimit()
sys.setrecursionlimit(100000)

with open('8/task8_input.txt', 'r') as f:
    input = f.read()

input = input.strip('\n')
input = input.split(' ')
input = [int(i) for i in input]


def findMetaSum(list):
    # print(list)
    children = list.pop(0)
    meta = list.pop(0)
    mdsum = 0

    for i in range(children):
        mdsum += findMetaSum(list)

    for i in range(meta):
        mdsum += list.pop(0)
    # print('Sum: ' + str(mdsum))
    return mdsum


print("Task 1: " + findMetaSum(input))


def nodeValue(list):
    children = list.pop(0)
    meta = list.pop(0)
    value = 0
    meta_list = []
    # When meta is 0 needs to be added
    values = {0: 0}

    if children == 0:
        for i in range(meta):
            value += list.pop(0)
    else:
        for i in range(children):
            values[i + 1] = nodeValue(list)

        for i in range(meta):
            meta_list.append(list.pop(0))

        for i in meta_list:
            if i <= children:
                value += values[i]

    return value


print("Task 2: " + str(nodeValue(input)))
