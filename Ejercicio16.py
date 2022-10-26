diccionario = {
    1 : "Castillo", 15 : "Ramos",
    3 : "Pique", 5 : "Puyol",
    11 : "Capdevila", 14 : "Xabi",
    16 : "Buquets", 8 : "Xavi Hernandez",
    18 : "Pedrito", 6 : "Iniesta",
    7 : "Villa"
}

OpcionJugador = int(input("Ingresa el numero de jugador: "))

if OpcionJugador in diccionario:
    print(diccionario[OpcionJugador])
else:
    print("No es un numero del diccionario")
