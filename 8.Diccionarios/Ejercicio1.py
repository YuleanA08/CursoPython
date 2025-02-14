'''Ejercicio 1
En el siguiente diccionario se encuentran capitales de los paises en
el mundo, debes realizar un programa que pida un pais al usuario, y
muestre la capital de ese pais, en dado caso el pais no este en el dic
cionario, se debe mostrar un mensaje diciendo que ese pais no se en
cuentra.'''

DiccionarioPaises = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

Paises = input("Ingresa el nombre de un pais: ")

if Paises in DiccionarioPaises.keys():
    print("La capital del pais: "+ Paises + "es: " + DiccionarioPaises[Paises])
else:
    print("Este pais", Paises, "no se encuentra en nuestra base de datos")