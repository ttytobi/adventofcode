import sys
sys.path.append('../')
from Timer.mytimer import performance

with open(sys.argv[-1], 'r') as f:
    raw = f.read().split('\n')

@performance
def get_matched(data):
    result = 0
    for game in data:
        sep = game.split('|')
        draws = [num.strip() for num in sep[1].split(' ') if num]
        winning = [num.strip() for num in sep[0].split(':')[1].split(' ') if num]
        matches = list(set(winning).intersection(draws))
        if not matches:
            pass
        elif len(matches) == 1:
            result += 1
        else:
            a = 1
            for i, _ in enumerate(range(1, len(matches))):
                a += 2**i
            result += a
    return result

print(f'Solution Part 1: {get_matched(raw)}')