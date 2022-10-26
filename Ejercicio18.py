numero = int(input("Ingresa un numero para multiplicar: "))

i = 0
multi = 0

while i <= 10:
    multi = numero * i
    print("{} x {} = {}".format(numero , i , multi))
    i += 1