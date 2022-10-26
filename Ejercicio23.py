def numeros():
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    if num1 > num2:
        return 1
    elif num2 > num1:
        return -1
    else:
        return 0

print(numeros())
