def check(arr):
    low = []
    for c in arr:
        if c.islower():
            low.append(c)
    for i in range(len(low) - 1):
        if low[i] > low[i + 1]:
            return False
    return True


arrays = [
    ['a', 'B', 'c', 'D', 'e'],
    ['z', 'a', 'b'],
    ['A', 'B', 'C'],
    ['a', 'a', 'b', 'x'],
    ['m', 'k', 'Z'],
]

for i in range(5):
    if check(arrays[i]):
        print(i + 1)
    else:
        print(-1)
