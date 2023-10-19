a = [1,2,2,4]
flag = 0
if len(set(a)) == 1:
    print("Все числа равны")
elif len(set(a)) == len(a):
    print("Все числа разные")
else:
    print( "Есть равные и неравные числа")