while True:
    N = int(input())
    if N == 0:
        break

    b = list(map(int, input().split()))
    cnt = 0
    while cnt <= 10000:
        isTriangle = True
        if b[0] != 1:
            isTriangle = False
        for i in range(1, len(b)):
            if b[i] != b[i - 1] + 1:
                isTriangle = False
                break
        if isTriangle:
            break

        tmp = list()
        for num in b:
            if num > 1:
                tmp.append(num - 1)

        tmp.append(len(b))
        b = tmp
        cnt += 1

    if cnt <= 10000:
        print(cnt)
    else:
        print(-1)


