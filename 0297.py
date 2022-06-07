N = int(input())
for i in range(N):
    K, P = map(int, input().split())
    if K % P != 0:
        print(K % P)
    else:
        print(P)
