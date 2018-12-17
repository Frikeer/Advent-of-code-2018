input = 9445

# Calculate powerlevel


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


power_levels = {(x, y, 1): getPowerLevel((x, y), input)
                for x in range(1, 301) for y in range(1, 301)}


def getPowerTotals(top_left, power_levels, size):
    total = 0
    for x in range(size):
        for y in range(size):
            total += power_levels[top_left[0] + x, top_left[1] + y]
    return total


square_size = 3
total_power_levels = {(x, y, 3): getPowerTotals((x, y), power_levels, square_size)
                      for x in range(1, 298) for y in range(1, 298)}


def maxKey(dict):
    v = list(dict.values())
    k = list(dict.keys())
    return k[v.index(max(v))]


print("Largest 3x3 cell: " + str(maxKey(total_power_levels)))

max_size = 300

