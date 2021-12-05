#Ejercicio 09
frase =input("Introduce  una frase: ")
letra =input("Introducxe una letra: ")
contador = 0
for x in frase:
    if x == letra:
        contador = contador + 1
print("La letra aparece",contador,"veces en la frase")
