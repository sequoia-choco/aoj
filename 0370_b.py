from re import A


a = list(map(int, input().split()))
b = list(map(int, input().split()))
tmp = list()

if a > b:
    tmp = a
    a = b
    b = tmp

if a[1:] < b[1:]:
    print(b[0] - a[0] + 1)
else:
    print(b[0] - a[0])
