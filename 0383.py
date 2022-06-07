A, B, X = map(int, input().split())

answer = list()
for a in range(21):
    for b in range(41):
        total = a * 1000 + b * 500
        if total >= X:
            answer.append((A * a + B * b, a, b))

answer_sorted = sorted(answer, key=lambda x: x[0])
print(answer_sorted[0][0])
