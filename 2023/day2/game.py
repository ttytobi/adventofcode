import sys

with open(sys.argv[-1], 'r') as f:
    raw = f.read().split('\n')

limits = {
    "red": 12,
    "blue": 14,
    "green": 13
}

games = []
for line in raw:
    game_id, draw = line.split(':')
    for subset in draw.split(';'):
        dice_col = [] # [['3', 'green'], ['3', 'blue'], ['6', 'red']]
        for dice in subset.split(','):
            dice_col.append(dice.split())
        dice_val = {} # {'green': 3, 'blue': 3, 'red': 6}
        for y,x in dice_col:
            dice_val[x] = int(y)
        # if any of the values exceeds the limit -> break. Default to 0 if color is not present
        if dice_val.get("red",0) > int(limits["red"]):
            break
        elif dice_val.get("blue",0) > int(limits["blue"]):
            break
        elif dice_val.get("green",0) > int(limits["green"]):
            break
        else:
            pass
    else:
        games.append(int(game_id.split()[-1]))

print(f'Part 1: {sum(games)}')

# [
# {'blue': 2, 'red': 3}, 
# {'green': 3, 'blue': 3, 'red': 6}, 
# {'blue': 4, 'red': 6}, 
# {'green': 2, 'blue': 2, 'red': 9}, 
# {'red': 2, 'blue': 4}
# ]

result = 0
for line in raw:
    joined = []
    game_id, draw = line.split(':')
    for subset in draw.split(';'):
        dice_col = [] # [['3', 'green'], ['3', 'blue'], ['6', 'red']]
        for dice in subset.split(','):
            dice_col.append(dice.split())
        dice_val = {} # {'green': 3, 'blue': 3, 'red': 6}
        for y,x in dice_col:
            dice_val[x] = int(y)
        joined.append(dice_val)
    # Go thru joined dicts. If blue, green, red is not in "sorted", add it. Then add the values to the list that is in each key
    sorted = {}
    for dicts in joined:
        for key in dicts:
            if key not in sorted:
                sorted[key] = []
            sorted[key].append(dicts[key])
    # {'blue': [10, 12, 15, 15, 6], 'red': [8, 10, 17, 16, 1, 9], 'green': [12, 9, 3, 12, 6, 10]}
    # For each key get the highest element of the list -> multiply -> sum up.
    result += int(max(sorted["green"])) * int(max(sorted["red"])) * int(max(sorted["blue"]))

print(f'Part 2: {result}')
