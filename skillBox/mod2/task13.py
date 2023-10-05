barcode = input()
if len(barcode) !=13:
    print("no")
odd_sum = 0
even_sum = 0
for i in range(len(barcode)):
    digit = int(barcode[i])
    if i % 2 == 0:
        odd_sum += digit
    else:
        even_sum += digit * 3
if (odd_sum + even_sum) % 10 == 0:
    print("yes")
