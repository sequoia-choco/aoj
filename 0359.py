week_of_day = ["fri", "sat", "sun", "mon", "tue", "wed", "thu"]

X = int(input())

print(week_of_day[(X % 7) - 1])

