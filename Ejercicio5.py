from math import sqrt

A = int(input("ingresa el valor de A: "))
B = int(input("ingresa el valor de B: "))
C = int(input("ingresa el valor de C: "))

X1 = 0
X2 = 0

if ((B**2)-(4*A*C)) < 0:
    print("No se puede realizar por que no se puede sacar raiz a un numero 0")
else:
    x1 = (-B + sqrt((B**2)-(4*A*C)))/(2*A)
    x2 = (-B - sqrt((B**2)-(4*A*C)))/(2*A)
    print("La solucion es: \nx1",x1, "\nx2", x2)