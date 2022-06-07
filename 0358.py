m, f, b = map(int, input().split())

answer = 0
if (b - m) > 0:
    if (b - m) <= f:
        answer = b - m
    else:
        answer = 'NA'

print(answer)
