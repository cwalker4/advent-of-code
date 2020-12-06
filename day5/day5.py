from math import floor, ceil
import numpy as np

with open('input.txt', 'r') as f:
    arr = f.read().splitlines()

def get_pos(s, nmax):
    # takes s (str) the binary partition string, and nmax (int) the max number of seats
    low = 0
    high = nmax - 1
    for i in s:
        if i in ('F', 'L'):
            high = floor((low + high) / 2)
        elif i in ('B', 'R'):
            low = ceil((low + high) / 2)
    return low

def get_seatid(row, col):
    return (row * 8) + col

row_max = 128
col_max = 8
seatids = []
filled_seats = np.full((row_max, col_max), 0)

# part 1
for seat in arr:
    # get the row and column
    row, col = get_pos(seat[:7], row_max), get_pos(seat[-3:], col_max)
    
    # update arrays
    filled_seats[row, col] = 1
    seatids.append(get_seatid(row, col))

print(f"Max seat ID: {max(seatids)}")

# part 2
for row, col in np.argwhere(filled_seats == 0):
    seatid = get_seatid(row, col)
    if seatid - 1 in seatids and seatid + 1 in seatids:
        break
        
print(f"My seat: ({row}, {col}), ID = {get_seatid(row, col)}")

