a = 'СЕВЕР'
b = 'ЮГ'
c = 'ЗАПАД'
d = 'ВОСТОК'
x = 0
y = 0
n = 10000
for i in range(n):
    side = input()
    if side == a:
        num = int(input())
        y += num
    elif side == b:
        num = int(input())
        y -= num
    elif side == c:
        num = int(input())
        x -= num
    elif side == d:
        num = int(input())
        x += num
    elif side == 'СТОП':
        break

print(x, ';', y)