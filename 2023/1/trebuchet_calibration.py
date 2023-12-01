import regex as re
### part 1

with open('input', 'r') as f:
    data = f.read().strip()

def add_up(list):
    new = []
    for item in list:
        if len(item) == 1:
            new.append(int(f'{item}{item}'))
        else:
            new.append(int(f'{item[0]}{item[-1]}'))
    return new

nums = [str(''.join([n for n in x if n.isdigit()])) for x in data.split("\n")]
#print(nums)

print(f'Part 1: {sum((add_up(nums)))}')

# part2... lots of stackoverflow, not happy how long that took :( and pretty sure it's a mess.
# Was not aware of regex and the overlapped=True field.

num_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

new = []
for line in data.split("\n"):
    find = re.findall(r'one|two|three|four|five|six|seven|eight|nine|\d', line, overlapped=True)
    new.append(''.join(list(map(str, [num_dict.get(n, n) for n in find]))))

nums1 = [''.join([n for n in x if n.isdigit()]) for x in new]

print(f'Part 2: {sum((add_up(nums1)))}')