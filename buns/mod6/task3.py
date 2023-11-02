def get_armstrong_numbers():
    n = 10
    while True:
        h = [int(d) for d in str(n)]  # разбиваем число на отдельные цифры
        l = len(h)
        if sum(j**l for j in h) == n:
            yield n
        n += 1

generator = get_armstrong_numbers()
for i in range(8):
    print(next(generator), end=' ')