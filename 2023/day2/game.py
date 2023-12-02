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

print(sum(games))