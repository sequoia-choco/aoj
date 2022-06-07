grid = [[0 for i in range(2000)] for j in range(2000)]

for i in range(2):
    x, y, w, h = map(int, input().split())
    for i in range(x, x + w):
        for j in range(y, y + h):
            grid[i][j] += 1

count = 0
for i in range(2000):
    for j in range(2000):
        if grid[i][j] == 1:
            count += 1

print(count)
