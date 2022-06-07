A, B, X = map(int, input().split())

ans = list()
for i in range(1001):
    for j in range(1001):
        if 1000 * i + 500 * j >= X:
            ans.append(A * i + B * j)

ans_sorted = sorted(ans)
print(ans_sorted[0])
