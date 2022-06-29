def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

W, H, C = map(int, input().split())
print((W // gcd(W, H)) * (H // gcd(W, H)) * C)
