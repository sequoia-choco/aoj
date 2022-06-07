d = int(input())
angle = d // 3600
minute = (d % 3600) // 60
second = (d % 3600) % 60
print(f'{angle} {minute} {second}')
