import re

with open('input.txt', 'r') as f:
    arr = f.read().split('\n\n')

n_yes = 0
for group in arr:
    letters = set(re.findall('[a-z]', group))
    n_yes += len(letters)

print(f"Part 1: {n_yes}")

n_yes = 0
for group in arr:
    answers = [set(x) for x in group.rstrip().split('\n')]
    common = set.intersection(*answers)
    n_yes += len(common)

print(f"Part 2: {n_yes}")
