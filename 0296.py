l = input().split()
l_i = [int(s) for s in l]
coin = [1, 5, 10, 50, 100, 500]

wallet = 0
for i in range(len(l_i)):
    wallet += l_i[i] * coin[i]

answer = 0
if wallet >= 1000:
    answer = 1

print(answer)
