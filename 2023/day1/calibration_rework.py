import regex as re
import sys
sys.path.append('../')
from Timer.mytimer import performance

with open(sys.argv[-1], 'r') as f:
    data = f.read().strip()

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

@performance
def first(fdata):
    result = 0
    count = 0
    for line in fdata.split("\n"):
        f = re.findall(r'\d', line)
        result += int(f[0] + f[-1])
        count += 1
    return result, count

@performance
def second(fdata):
    result = 0
    count = 0
    for line in fdata.split("\n"):
        f = re.findall(r'one|two|three|four|five|six|seven|eight|nine|\d', line, overlapped=True)
        translated = ''.join(list(map(str, [num_dict.get(n, n) for n in f])))
        result += int(translated[0] + translated[-1])
        count += 1
    return result, count

if __name__ == '__main__':
    print(f'First: {first(data)}')
    print(f'Second: {second(data)}')

# ~ py3 calibration_rework.py <name_of_input_file>