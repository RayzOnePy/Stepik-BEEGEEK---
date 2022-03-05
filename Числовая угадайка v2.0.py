import random
print('Добро пожаловать в игру "угадайка".\nТвоя задача угадать случайное число')
def game():
    counter_fails = 0
    print("Укажи диапозон от x до y")
    while True:
        x, y = input("Введи x:"), input("Введи y:")
        if x.isdigit() and y.isdigit():
            x, y = int(x), int(y)
            if x > y:
                x, y = y, x
            break
        else:
            print("Вводить нужно целое число")
    number = random.randint(x, y)
    print(f"Отлично. Теперь введи целое число в диапозоне от {x} до {y}")
    while True:
        guess = input("Целое число:")
        if is_valid(guess, x, y):
            guess = int(guess)
            if guess < number:
                print(f"Загаданное число больше {guess}")
            elif guess > number:
                print(f"Загаданное число меньше {guess}")
            elif guess == number:
                print(f"Харош, все верно! загаданное число было {number}")
                answer = input('Хочешь ссыграть еще раз? "Да"/"Нет" ')
                if answer.lower() == "да":
                    game()
                elif answer.lower() == "нет":
                    print("Хорошо, приходи когда захочешь снова поиграть. Спасибо за игру!)")
                    return False
                else:
                    print("Либо да, либо нет. Третьего не дано")
        else:
            counter_fails += 1
            if counter_fails == 1:
                print(f"Обьясняю еще раз. Ввести надо ЦЕЛОЕ ЧИСЛО в диапозоне от {x} до {y}")
            elif counter_fails == 2:
                print("Издеваешься?")
            elif counter_fails == 3:
                print("У тебя осталась последняя попытка")
            elif counter_fails == 4:
                print(f"Видимо ты не хочешь играть. Ладно приходи когда появиться желание\nесли тебе интересно,загаданное число было {number}")
                break

def is_valid(number, x, y):
    if number.isdigit() and x <= int(number) <= y:
        return True
    else:
        return False

game()