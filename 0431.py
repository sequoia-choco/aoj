N = int(input())
ri = list(map(int, input().split()))

ri_reversed = list(reversed(ri))
count = 1
ri_max = ri_reversed[0]

for i in range(1, N):
    if ri_reversed[i] > ri_max:
        ri_max = ri_reversed[i]
        count += 1

print(count)
