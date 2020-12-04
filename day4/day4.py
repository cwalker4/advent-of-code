import re
import numpy as np

# functions
def parse_line(entry):  
    # split on whitespace or newlines
    full = re.split('[\s\n]', entry)
    
    # remove empty strings
    full = [s for s in full if s]
    
    # break into keys and values
    keyvals = np.transpose([x.split(':') for x in full])
    keys, values = keyvals[0], keyvals[1]
    
    # return dict
    return dict(zip(keys, values))

def has_req_fields(entry):
    req_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    missing = req_fields - set(entry.keys())
    return len(missing) == 0

def validate_field(field, value):
    # expects field (str) and value (str), return True if valid, False otherwise
    if field == 'byr':
        if not value.isdigit():
            return False
        return int(value) in range(1920, 2003)

    if field == 'iyr':
        if not value.isdigit():
            return False
        return int(value) in range(2010, 2021)

    if field == 'eyr':
        if not value.isdigit():
            return False
        return int(value) in range(2020, 2031)

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


