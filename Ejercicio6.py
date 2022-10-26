practica1 = float(input("Ingrese el valor de la preactica 1: "))
practica2 = float(input("Ingrese el valor de la preactica 2: "))
practica3 = float(input("Ingrese el valor de la preactica 3: "))
ExamenParcial = float(input("ingrese el valor del examen Parcial: "))
ExamenFinal = float(input("Ingrese el valor del examen Final: "))

PromedioPractica = (practica1 + practica2 + practica3)/3
PromedioFinal = (PromedioPractica + 2*ExamenParcial + 3*ExamenFinal)/6

print("El promedio final del estudiante es de\n: ", PromedioPractica, "\n Y el promedio Final es de:\n", PromedioFinal)
