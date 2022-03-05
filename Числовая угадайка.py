import random
number = random.randint(1, 100)
counter_fails = 0
print("Добро пожаловать в числовую угадайку")
print("Ваша задача - угадать целое число от 1 до 100")
def is_valid(number):
    if number.isdigit() and 1 <= int(number) <= 100:
        return True
    else:
        return False
while True:
    guess = input("Введите целое число от 1 до 100")
    if is_valid(guess):
        guess = int(guess)
        if guess > number:
            print("Загаданное число меньше")
        elif guess < number:
            print("Загаданное число больше")
        elif guess == number:
            print(f"Поздравляю, ты отгадал число. Загаданное число было {number}")
            break
    else:
        counter_fails += 1
        if counter_fails == 1:
            print("Число находится в диапозоне от 1 до 100. Попробуй отгадать)")
        elif counter_fails == 3:
            print("Издеваешься?")
        elif counter_fails == 4:
            print("У тебя последняя попытка отгадать ЧИСЛО")
        elif counter_fails == 5:
            print("Ввидимо ты не хочешь играть. Ладно, приходи когда появится желание")
            break
        else:
            print("Ты видимо не понял. Тебе нужно отгадать целое число в диапозоне от 1 до 100. Попробуй снова")
            