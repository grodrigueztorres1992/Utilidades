print(abs(-5))

numero = int(input("Ingresa numero entero: "))

if numero > 0:
    print("El valor absoluto de {} es: {}".format(numero, numero))
else:
    print("El valor absoluto de {} es: {}".format(numero, abs(numero)))
