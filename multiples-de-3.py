lista = []
for numero in range(1, 101):
    if numero % 3 == 0:
        lista.append("Fizz")
    else:
        lista.append(numero)
print (lista)
