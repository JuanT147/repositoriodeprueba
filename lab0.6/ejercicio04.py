cantidad  =int(input("Cual es la cantidada a invertir: "))
interes =float(input("Cual es interes anual: "))
#Ejercicio 04
años = int(input("Cuantos años desea invertir: "))
for x in range(1,años+1):
    capital =cantidad*(1 + interes)**x
    print("El capital optenido durante {} años es".format(x),capital)

