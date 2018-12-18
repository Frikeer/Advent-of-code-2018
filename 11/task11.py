input = 9445

# Calculate powerlevel for a cell


def getPowerLevel(cell, input):
    rackID = cell[0] + 10
    power = rackID * cell[1]
    power += input
    power *= rackID
    try:
        power = int(str(power)[len(str(power)) - 3]) - 5
    except:
        power = 0

    return power


# Get power level for all cells
power_levels = {(x, y, 1): getPowerLevel((x, y), input)
                for x in range(1, 301) for y in range(1, 301)}

# Get total power levels of squares with top left cord (x,y)


def getPowerTotals(top_left, power_levels, size):
    total = 0
    for x in range(size):
        for y in range(size):
            total += power_levels[top_left[0] + x, top_left[1] + y, 1]
    return total


square_size = 3
total_power_levels = {(x, y, square_size): getPowerTotals((x, y), power_levels, square_size)
                      for x in range(1, 298) for y in range(1, 298)}

# Get the key of the max value


def maxKey(dict):
    v = list(dict.values())
    k = list(dict.keys())
    return k[v.index(max(v))]


print("Largest 3x3 cell: " + str(maxKey(total_power_levels)))


# Part 2:


def get_xrows():
    rows = {}
    for x in range(1, 301):
        row_val = [0 for y in range(1, 301)]
        for y in range(1, 301):
            row_val[y - 1] += power_levels[x, y, 1]
        rows[x] = row_val
    return rows


def get_yrows():
    rows = {}
    for y in range(1, 301):
        row_val = [0 for x in range(1, 301)]
        for x in range(1, 301):
            row_val[x - 1] += power_levels[x, y, 1]
        rows[y] = row_val
    return rows


xrows = get_xrows()
yrows = get_yrows()
max_size = 300

power_levels_size = power_levels

# Use s-1 and only add the x and y rows
for s in range(2, max_size + 1):
    for x in range(1, 301 + 1 - s):
        for y in range(1, 301 + 1 - s):
            power_levels_size[x, y, s] = power_levels_size[x, y, s - 1] + \
                sum(xrows[x + s - 1][y - 1:y - 1 + s]) + \
                sum(yrows[y + s - 1][x - 1:x - 2 + s])

print("Largest nxn cell(x,y,n): " + str(maxKey(power_levels_size)))
