n = int(input("introduce un numero: "))

i = 1

while i <= n:
    if i < n:
        print(i, end=",")
    else:
        break
    i += 1
print(i)