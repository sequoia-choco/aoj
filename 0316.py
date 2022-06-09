h = list(map(int, input().split()))
k = list(map(int, input().split()))
a, b, c, d = map(int, input().split())

def score(l: list) -> int:
    # total = 0
    total = a * l[0] + b * l[1]
    if l[0] >= 10:
        total += c * (l[0] // 10)
    if l[1] >= 20:
        total += d * (l[1] // 20)
    return total

if score(h) == score(k):
    print("even")
elif score(h) > score(k):
    print("hiroshi")
else:
    print("kenjiro")
