def search(x, y):
    X_MIN = 0
    Y_MIN = 0
    X_MAX = 0
    Y_MAX = 0
    f = 0
    f1 = 1
    f2 = 0
    p = 0
    while True:
        if (X_MIN <= x and x <= X_MAX) and (Y_MIN <= y and y <= Y_MAX):
            return p % 3 + 1
        f = f1 + f2
        if p % 4 == 0:
            X_MAX += f
        elif p % 4 == 1:
            Y_MAX += f
        elif p % 4 == 2:
            X_MIN -= f
        else:
            Y_MIN -= f
        p += 1
        f2 = f1
        f1 = f

x, y = map(int, input().split())
print(search(x, y))
