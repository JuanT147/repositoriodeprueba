#Ejercicio 02
numero = int(input("Introduce un numero positivo: "))
if numero >0:
    impares= []
    for x in range(numero):
        if x %2 == 1:
            impares.append(x)
    print(*impares, sep=",")        
        
else:
    print("Introduce un numero correcto")  
    print("Fin del programa")
