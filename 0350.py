def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def printV(x, y):
    g = gcd(x, y)
    print(str(x // g) + "/" + str(y // g))

S = input()
o = S.find(".")
p = S.find("(")
d = len(S) - o - 1

if p == -1:
    all = S[0:o] + S[o + 1:len(S)]
    printV(int(all), 10 ** d)
else:
    sub = S[0:o] + S[o + 1:p]
    all = sub + S[p + 1:len(S) - 1]
    l = p - o - 1
    d -= 2
    printV(int(all) - int(sub), 10 ** d - 10 ** l)
