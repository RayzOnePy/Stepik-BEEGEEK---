eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

def cipher(direction, language, step, text):
    if direction == "шифровать":
        final_text = ""
        if language == "ru":
            for i in range(len(text)):
                if text[i].isalpha():
                    if text[i] == text[i].lower():
                        if step > 31 - rus_lower_alphabet.index(text[i]):
                            final_text += rus_lower_alphabet[(rus_lower_alphabet.index(text[i]) + step) % 31 - 1]
                        else:
                            final_text += rus_lower_alphabet[rus_lower_alphabet.index(text[i]) + step]
                    elif text[i] == text[i].upper():
                        if step > 31 - rus_upper_alphabet.index(text[i]):
                            final_text += rus_upper_alphabet[(rus_upper_alphabet.index(text[i]) + step) % 31 - 1]
                        else:
                            final_text += rus_upper_alphabet[rus_upper_alphabet.index(text[i]) + step]
                else:
                    final_text += text[i]

        if language == "eng":
            for i in range(len(text)):
                if text[i].isalpha():
                    if text[i] == text[i].lower():
                        if step > 25 - eng_lower_alphabet.index(text[i]):
                            final_text += eng_lower_alphabet[(eng_lower_alphabet.index(text[i]) + step) % 25 - 1]
                        else:
                            final_text += eng_lower_alphabet[eng_lower_alphabet.index(text[i]) + step]
                    elif text[i] == text[i].upper():
                        if step > 25 - eng_upper_alphabet.index(text[i]):
                            final_text += eng_upper_alphabet[(eng_upper_alphabet.index(text[i]) + step) % 25 - 1]
                        else:
                            final_text += eng_upper_alphabet[eng_upper_alphabet.index(text[i]) + step]
                else:
                    final_text += text[i]
    
    if direction == "дешифровать":
        final_text = ""
        if language == "ru":
            for i in range(len(text)):
                if text[i].isalpha():
                    if text[i] == text[i].lower():
                        if step - 1 >= rus_lower_alphabet.index(text[i]):
                            final_text += rus_lower_alphabet[(rus_lower_alphabet.index(text[i]) - (step % 32))]
                        else:
                            final_text += rus_lower_alphabet[rus_lower_alphabet.index(text[i]) - step]
                    elif text[i] == text[i].upper():
                        if step - 1 >= rus_upper_alphabet.index(text[i]):
                            final_text += rus_upper_alphabet[(rus_upper_alphabet.index(text[i]) - (step % 32))]
                        else:
                            final_text += rus_upper_alphabet[rus_upper_alphabet.index(text[i]) - step]
                else:
                    final_text += text[i]

        if language == "eng":
            for i in range(len(text)):
                if text[i].isalpha():
                    if text[i] == text[i].lower():
                        if step - 1 >= eng_lower_alphabet.index(text[i]):
                            final_text += eng_lower_alphabet[(eng_lower_alphabet.index(text[i]) - (step % 26))]
                        else:
                            final_text += eng_lower_alphabet[eng_lower_alphabet.find(text[i]) - step]
                    elif text[i] == text[i].upper():
                        if step - 1 >= eng_upper_alphabet.index(text[i]):
                            final_text += eng_upper_alphabet[(eng_upper_alphabet.index(text[i]) - (step % 26))]
                        else:
                            final_text += eng_upper_alphabet[eng_upper_alphabet.find(text[i]) - step]
                else:
                    final_text += text[i]
    print(f"Начальный текст : {text}")
    print(f"Конечный текст : {final_text}")

while True:
    direction = input("Выберите шифровать/дешифровать").lower()
    while direction != "шифровать" and direction != "дешифровать":
        direction = input("Неправильно.\nВыберите шифровать/дешифровать").lower()

    language = input("Выберите язык eng/ru").lower()
    while language != "eng" and language != "ru":
        language = input("Неправильно.\nВыберите язык eng/ru ")

    step = input("Укажите шаг сдвига(целое число)")
    while step.isdigit() == False and int(step) < 0:
        step = input("Неправильно.\nУкажите шаг сдвига(целое число)")
    step = int(step)
    if language == "ru" and int(step) > 32:
        step = int(step) % 32
    if language == "eng" and int(step) > 26:
        step = int(step) % 26


    text = input("Введите текст")
    cipher(direction, language, step, text)
    repeat = input("Еще раз?")
    if repeat.lower() != "да" and repeat.lower() != "нет":
        repeat = input("Либо да, либо нет")
    if repeat.lower() == "нет":
        break