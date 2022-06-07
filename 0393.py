H, A, B = map(int, input().split())

count = 0
for i in range(A, B+1, 1):
    if H % i == 0:
        count += 1

print(count)
