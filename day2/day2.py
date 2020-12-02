import re

# part 1
n = 0
with open('input.txt', 'r') as f:
    for line in f:
        l, h, letter, pwd = re.split('[^A-Za-z0-9]+', line)[:-1]
        l, h = int(l), int(h)
        
        if len(re.findall(letter, pwd)) in range(l, h + 1):
            n += 1
            
print(f"For Part 1 there are {n} correct passwords")

# part 2
n = 0
with open('input.txt', 'r') as f:
    for line in f:
        l, h, letter, pwd = re.split('[^A-Za-z0-9]+', line)[:-1]
        l, h = int(l), int(h)
        
        try:
            l_letter = pwd[l-1]
            h_letter = pwd[h-1]
        except IndexError:
            continue
        
        if (l_letter == letter) != (h_letter == letter):
            n += 1

print(f"For Part 2 there are {n} correct passwords")

