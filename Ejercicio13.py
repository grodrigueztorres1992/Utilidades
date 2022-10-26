lista = [20 , 50 , "Curso" , 'Python' , 3.14]
print("Estos son los valores actuales de la lista: ", lista)

palabra1 = input("Ingrese el primer valor para sustituir en el espacio 1: ")
palabra2 = input("Ingrese el seguindo valor para sustituir en el espacio 2: ")

lista[0] = palabra1
lista[1] = palabra2

print("El valor de la lista es: {}".format(lista))