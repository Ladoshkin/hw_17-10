i = 0
a = 0
n=50
up = 101
down = 1
while a < 3:
    print('Ваше число 1 меньше, 2 больше, 3 равно: ',n)
    a = int(input())
    i += 1
    if a == 1 :
        up = n
        n = (down + up) // 2
    elif a == 2:
        down = n
        n = (down + up) // 2
    else:
        print('Ваше число:', n)
print("Число угадано за",i,"попыток")
