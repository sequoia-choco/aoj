N = int(input())
x = list(map(int, input().split()))

def solve(l: list) -> int:
    total = 0
    L = min(l[1:])
    R = max(l[1:])
    total = R - L
    if abs(L - x[0]) <= abs(R - x[0]):
        total += abs(L - x[0])
    else:
        total += abs(R - x[0])
    return total

print(solve(x))
