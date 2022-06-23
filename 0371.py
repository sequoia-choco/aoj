n = int(input())
maxt = 0
t = []
for i in range(n):
    t.append(int(input()))
    if t[i] > maxt:
        maxt = t[i]

divisors = []
for i in range(1, maxt + 1):
    if maxt % i == 0:
        divisors.append(i)

ans = 0
for num in t:
    for d in divisors:
        if d >= num:
            ans += d - num
            break

print(ans)
