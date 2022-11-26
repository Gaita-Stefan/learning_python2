lista=[7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(sorted(lista))
print(sorted(lista, reverse=True))
print(lista[0::2])
print(lista[1::2])
for x in lista:
    if x%3==0:
        print(x)