with open('day1/input.txt', 'r') as f:
    arr = f.read().splitlines()

arr = [int(x) for x in arr]

def two_sum(arr, x):
    arr.sort()
    l = 0
    h = len(arr) - 1
    while l < h:
        if arr[l] + arr[h] == x:
            return arr[l] * arr[h]
        elif arr[l] + arr[h] < x:
            l += 1
        else:
            h -= 1
    return -1

def three_sum(arr, x):
    arr.sort()
    l = 0
    h = len(arr) - 1
    for y in arr:
        tmp = two_sum(arr, x - y)
        if tmp != -1:
            return tmp * y

print(f"Two Numbers: {two_sum(arr, 2020)}")
print(f"Three Numbers: {three_sum(arr, 2020)}")
