letra = input("Ingresa una letra: ")
'''
if letra.lower() == "a":
    print("Es una vocal")

else:
    if letra.lower() == "e":
        print("Es una vocal")
    else:
        if letra.lower() == "i":
            print("es una vocal")
        else:
            if letra.lower() == "o":
                print("Es una vocal")
            else:
                if letra.lower() == "u":
                    print("Es una vocal")
                else:
                    print("No es una Vocal")
'''    
#lo mismo que esta arriba pero con in busca dentro de las comillas
if letra.lower() in "aeiou":
    print("Es una vocal")
else:
    print("No es una vocal")