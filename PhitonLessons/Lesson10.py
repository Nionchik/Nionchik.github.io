import random
num = random.randint(1, 100)
while True:
    print("Угадай число от 1 до 100")
    quess = input()
    i = int(quess)
    if i == num:
        print('Правильно!')
        break
    elif i < num:
        print("Загаданное число больше")
    elif i > num:
        print("Загаданное число меньше")