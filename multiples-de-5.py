# Generar la lista del 1 al 100 y cambia los multiples de 5 por cola
lista = []

for i in range(1, 101):
    if i % 5 == 0:
        lista.append("Buzz")
    else:
        lista.append(i)

# Imprimir la lista generada
print(lista)