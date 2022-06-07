h, r = map(int, input().split())
# if h < 0 and h + r == 0:
#     print(0)
# elif h < 0 and h + r < 0:
#     print(-1)
# else:
#     print(1)
if -h == r:
    print(0)
elif -h > r:
    print(-1)
elif -h < r:
    print(1)
