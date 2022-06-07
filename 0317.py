"""
l = input().split(' ')
l_i = [int(s) for s in l]
big_jump = l_i[0] // l_i[1]
small_jump = l_i[0] % l_i[1]
total = big_jump + small_jump
print(total)
"""

D, L = map(int, input().split())
print(D // L + D % L)
