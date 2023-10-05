s = input()
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м',
                  'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
s = s.lower()
v_count = 0
c_count = 0
for char in s:
    if char in vowels:
        v_count += 1
    elif char in consonants:
        c_count += 1
print(v_count, c_count)
