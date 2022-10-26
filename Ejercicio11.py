palabra1 = input("Ingresa la primer palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

if len(palabra1) < 3 or len(palabra2) < 3:#cuantos caracteres tiene palabra1 y palabra2
    print("No rima, porque tienen menos de 3 caracteres")
elif palabra1[-3 : ] == palabra2[-3 : ]:
    print("Las palabras riman")
elif palabra1[-2 : ] == palabra2[-2 : ]:
    print("Las palabras riman un poco")
else:
    print("Las palabras no riman")