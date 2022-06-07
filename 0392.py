# a, b = map(int, input().split())
# if a > b:
#     print(1)
# else:
#     if b % a == 0:
#         print(b // a)
#     else:
#         print(f'{(b // a) + 1}')

a, b = map(int, input().split())
ans = 1
if b > a :
    ans =  b // a
    if b % a == 0 :
        ans = ans
    else:
        ans += 1
print(ans)
# print(b // a + bool(b % a))
