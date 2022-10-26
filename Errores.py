while True:

    try:

        edad = int(input("Ingresa su edad: "))
        print("Tu edad es: " ,edad)
        break
    except:
        print("Ingresaste un valor erroneo")
    finally:
        print("La ejecucion ha finalizado")
