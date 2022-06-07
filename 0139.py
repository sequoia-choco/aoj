import re

A = ">'(=+)#\\1~$"
B = ">\^(Q=)+~~$"

for _ in range(int(input())):
    s = input()
    # r = re.match(A, s)
    if re.match(A, s):
        print("A")
    elif re.match(B, s):
        print("B")
    else:
        print("NA")
