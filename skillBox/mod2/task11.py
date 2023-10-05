def has_duplicate_digits(sequence):
    seen = set()
    for num in sequence:
        while num > 0:
            digit = num % 10
            if digit in seen:
                return True
            seen.add(digit)
            num //= 10
    return False

sequence = [0, 0, 1, 2, 3, 4, 5, 5, 6, 7]
result = has_duplicate_digits(sequence)
print(result)