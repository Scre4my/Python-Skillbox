a = int(input())
if a > 0:
    b_bin = bin(a)[2:]
    b_oct = oct(a)[2:]
    b_hex = hex(a)[2:]
    print(b_bin, b_oct,b_hex )
else:
    print("Неверный ввод")