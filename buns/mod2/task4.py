number = input("Введите натуральное число в десятичном коде: ")

try:
    a = int(number)
    if a <= 0:
        print("Неверный ввод")
    else:
        binary = bin(a)
        octal = oct(a)
        hexadecimal = hex(a)
        print("Двоичное представление:", binary[2:])
        print("Восьмеричное представление:", octal[2:])
        print("Шестнадцатеричное представление:", hexadecimal[2:])
except ValueError:
    print("Неверный ввод")