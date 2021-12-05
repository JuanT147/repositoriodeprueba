#Ejercicio 03
numero = int(input("Introduce un numero positivo: "))
if numero >0:
    todos= []
    for i in range(1,numero + 1):
        todos.append(i) 
    todos.reverse()
    print(*todos, sep=",")
else:
    print("Introduce un numero correcto")        