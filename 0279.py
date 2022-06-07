while True:
    N = int(input())
    if N == 0:
        break
    ki = list(map(int, input().split()))
    one_or_less = 0
    zero = 0
    for i in range(N):
        if ki[i] <= 1:
            one_or_less += 1
        if ki[i] == 0:
            zero += 1
    if N == one_or_less:
        print("NA")
    else:
        print(f'{N - zero + 1}')
