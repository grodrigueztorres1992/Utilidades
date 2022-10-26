


while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        print("Tu edad es: " ,edad)
        break
    except ValueError:
        print("has colocado un valor erroneo")
        break