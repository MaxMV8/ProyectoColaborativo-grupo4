# Generar la lista del 1 al 100
lista = []

for i in range(1, 101):
    if i % 5 == 0:
        lista.append("cola")
    else:
        lista.append(i)

# Imprimir la lista generada
print(lista)