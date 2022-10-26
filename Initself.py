"""class FabricaTelefonos():
    marca = "Samsung"

    def ElaborarHuawei(self):
        self.marca = "Huewei"

telefono = FabricaTelefonos()
print(telefono.marca)
telefono.ElaborarHuawei()
print(telefono.marca)"""

class FabricaTelefonos():
    def __init__(self , marca , color):
        self.marca = marca
        self.color = color
        print("Estoy ejecutando el metodo Init")
    
telefono = FabricaTelefonos("Huewei" , 'Negro')
print(telefono.marca)
print(telefono.color)