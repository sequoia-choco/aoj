ticket_price = [0, 6000, 4000, 3000, 2000]

for i in range(4):
    t, n = map(int, input().split())
    total = ticket_price[t] * n
    print(total)
