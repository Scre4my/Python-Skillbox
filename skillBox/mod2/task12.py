phone_number = input("Введите номер телефона: ")
cleaned_number = ''.join(filter(str.isdigit, phone_number))
print("Очищенный номер телефона:", cleaned_number)