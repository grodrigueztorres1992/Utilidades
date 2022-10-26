#

num1 = int(input("Ingresa el primer Numero: "))
num2 = int(input("Ingresa el segundo Numero: "))

for i in range(num1 , num2 + 1):
    if i % 2 == 0:#si el reciduo es igual igual a 0 salta al siguiente
        continue
    print(i)