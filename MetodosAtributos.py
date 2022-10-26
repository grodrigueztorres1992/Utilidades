class FabricaTelefonos():
    marca = "Huawei"
    color = "Negro"
    memoriaram = 32
    almacenamiento = 128

    def llamar(self , mensaje):
        return mensaje
    
    def escucharMusica(self):
        print("Estas escuchando musica")
telefono = FabricaTelefonos()

telefono.marca

print(telefono.llamar("Hola con quien hablo?"))
telefono.escucharMusica()
