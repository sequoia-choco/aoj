N = int(input())
A = [0] * (N + 1)
B = [0] * (N + 1)
C = [0] * (N + 1)

lineA = list(map(int, input().split()))
lineB = list(map(int, input().split()))
lineC = list(map(int, input().split()))

for i in range(1, lineA[0] + 1):
    A[lineA[i]] = 1
for i in range(1, lineB[0] + 1):
    B[lineB[i]] = 1
for i in range(1, lineC[0] + 1):
    C[lineC[i]] = 1

ans = 0
for i in range(N + 1):
    if (((not A[i]) and C[i]) or (B[i] and C[i])):
        ans += 1
print(ans)
