N = [1 for i in range(int(input()) + 1)]
A = [0 for i in range(len(N))]
B = [0 for i in range(len(N))]
C = [0 for i in range(len(N))]

aline = list(map(int, input().split()))
bline = list(map(int, input().split()))
cline = list(map(int, input().split()))

for i in range(1, aline[0] + 1):
    A[aline[i]] = 1

for i in range(1, bline[0] + 1):
    B[bline[i]] = 1

for i in range(1, cline[0] + 1):
    C[cline[i]] = 1

ans = 0
for i in range(1, len(N)):
    if ((not A[i] and C[i]) or (B[i] and C[i])):
        ans += 1
print(ans)
