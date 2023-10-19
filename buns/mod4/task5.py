filename = input()
with open(filename, 'r') as file:
    text = file.read()
letter_counts = {}
for letter in text:
    if letter.isalpha():
        letter = letter.lower()
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    # Сортировка словаря по значению (частоте)
sorted_counts = sorted(letter_counts.items(), key=lambda item: item[1])

# Записываем результат в файл
with open('result.txt', 'w') as file:
    for letter, count in sorted_counts:
        file.write(f"{letter}: {count}\n")
