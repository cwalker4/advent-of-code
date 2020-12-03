import numpy as np

with open('input.txt', 'r') as f:
    arr = f.read().splitlines()

def get_trees(arr, right, down):
    x = 0; y = 0
    xmax = len(arr[0]) 
    ymax = len(arr) - 1
    
    n_trees = 0
    while True:
        x  = (x + right) % xmax
        y += down

        if y > ymax:
            break
        if arr[y][x] == "#":
            n_trees += 1
            
    return n_trees

# part 1
right = 3
down = 1
n_trees = get_trees(arr, right, down)
print(f"Following right {right} and down {down} we hit {n_trees} trees")

# part 2
slopes = zip([1, 3, 5, 7, 1], [1, 1, 1, 1, 2])
trees = [get_trees(arr, x, y) for x, y in slopes]
tree_product = np.prod(trees)
print(f"Part two answer: {tree_product}")
