phone = input()
cleaned = ''.join(filter(str.isdigit, phone))
print(cleaned)