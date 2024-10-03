lista = []
for numero in range(1, 101):
    if numero % 3 == 0 and numero %5 == 0:
        lista.append("Coca")
    else:
        lista.append(numero)
print (lista)
