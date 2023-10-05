def shift_char(char, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    index = alphabet.index(char)
    shifted_index = (index + n) % len(alphabet)
    return alphabet[shifted_index]

i = input("Введите символ: ")
n = int(input("Введите число: "))

result = shift_char(i, n)
print("Символ после смещения:", result)
