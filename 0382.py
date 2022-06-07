N, C = map(int, input().split())
pi = list(map(int, input().split()))

total = sum(pi)
if total % (N + 1) == 0:
    print(total // (N + 1))
else:
    print(total // (N + 1) + 1)
