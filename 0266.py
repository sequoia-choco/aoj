G = [[1, 2], [-1, 3], [1, -1], [4, 5], [5, 2], [2, 1]]

while True:
    p = input()
    if p[0] == "#":
        break
    cur = 0
    for c in p:
        if cur == -1:
            break
        cur = G[cur][int(c)]
    print("Yes" if cur == 5 else "No")
