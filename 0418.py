MAX_X = 2000
MAX_Y = 2000

grid = [[0 for i in range(MAX_X)] for j in range(MAX_Y)]
for i in range(2):
    x, y, w, h = map(int, input().split())
    for i in range(x, x + w):
        for j in range(y, y + h):
            grid[i][j] = 1
            print(i, j)

count = 0
for i in range(MAX_X):
    for j in range(MAX_Y):
        if grid[i][j] == 1:
            count += 1

print(count)
