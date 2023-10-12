a = input()
a = a.split(" ")
f = ""
for i in range(len(a)):
    f += a[i][-1]
print(f)