import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

while True:
    chars = " "
    n = int(input("Количество паролей для генерации"))
    len = int(input("Длину одного пароля"))
    digit = input("Включать ли цифры 0123456789?(y/n)")
    if digit.lower() == "y":
        chars += digits
    lower_case = input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?(y/n)")
    if lower_case.lower() == "y":
        chars += lowercase_letters
    upper_case = input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?(y/n)")
    if upper_case.lower() == "y":
        chars += uppercase_letters
    symbols = input("Включать ли символы !#$%&*+-=?@^_?(y/n)")
    if symbols.lower() == "y":
        chars += punctuation
    if digit in ["y", "n"] and lower_case in ["y", "n"] and upper_case in ["y", "n"] and symbols in ["y", "n"]:
        break
    else:
        print("Неверно")

def generate_password(len, chars):
    password = ""
    for i in range(len):
        password += random.choice(chars)
    print(password)

for _ in range(n):
    generate_password(len, chars)
