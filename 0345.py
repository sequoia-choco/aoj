# l = input().split()
# l_i = [int(s) for s in l]
#
# answer = 'no'
# if ((l_i[0] == l_i[1]) and (l_i[2] == l_i[3])) \
#     or ((l_i[0] == l_i[2]) and (l_i[1] == l_i[3])) \
#     or ((l_i[0] == l_i[3]) and (l_i[1] == l_i[2])):
#     answer = 'yes'
#
# print(answer)

e1, e2, e3, e4 = map(int, input().split())
if e1 == e2 and e3 == e4 or e1 == e3 and e2 == e4 or e1 == e4 and e2 == e3:
    print('yes')
else:
    print('no')
