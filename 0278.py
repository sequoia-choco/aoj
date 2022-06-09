def cal(x, y, b, p):
    totals = []
    total = 0
    for i in range(b, 7):
        for j in range(p, 7):
            total = x * i + y * j
            if i >= 5 and j >= 2:
                total *= 0.8
            totals.append(int(total))
    return min(totals)

N = int(input())
for _ in range(N):
    x, y, b, p = map(int, input().split())
    print(cal(x, y, b, p))

# N = int(input())
# for _ in range(N):
#     x, y, b, p = map(int, input().split())
#     print(min(x * b + y * p, (x * max(b, 5) + y * max(p, 2)) * 4 // 5))
