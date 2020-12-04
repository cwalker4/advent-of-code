import re
import numpy as np

# functions
def parse_line(entry):  
    return {k: v for k, v in re.findall('([a-z]{3}):([^\s(\\n)]+)', entry)}

def has_req_fields(entry):
    req_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    missing = req_fields - set(entry.keys())
    return len(missing) == 0

def int_in_range(x, low, high):
    return x.isdigit() and int(x) >= low and int(x) <= high

def validate_field(field, value):
    # expects field (str) and value (str), return True if valid, False otherwise
    if field == 'byr':
        return int_in_range(value, 1920, 2002)

    if field == 'iyr':
        return int_in_range(value, 2010, 2020)
    
    if field == 'eyr':
        return int_in_range(value, 2020, 2030)

    if field == 'hgt':
        if not re.fullmatch('\d+(cm|in)', value):
            return False
        digit = int(re.findall('\d+', value)[0])
        unit = re.findall('cm|in', value)[0]
        if unit == 'cm':
            return digit in range(150, 194)
        if unit == 'in':
            return digit in range(59, 77)

    if field == 'hcl':
        return bool(re.fullmatch('#[a-f0-9]{6}', value))

    if field == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if field == 'pid':
        return bool(re.fullmatch('\d{9}', value))
    
def all_fields_correct(entry):
    for field in entry:
        # ignore country id field
        if field == 'cid':
            continue
        if not validate_field(field, entry[field]):
            return False
    return True

# read data
with open('input.txt', 'r') as f:
    raw = f.read().split('\n\n')
entries = [parse_line(x) for x in raw]

# part 1
n_valid = 0
for entry in entries:
    if has_req_fields(entry):
        n_valid += 1

print(f"Part 1: {n_valid} valid fields")

# part 2
n_valid = 0
for entry in entries:
    if has_req_fields(entry) and all_fields_correct(entry):
        n_valid += 1
        
print(f"Part 2: {n_valid} valid fields")


