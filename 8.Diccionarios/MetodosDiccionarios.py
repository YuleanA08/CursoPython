diccionario = {1:2, 2:3, 3:4 }
diccionario2= {4:5,5:6}
print(diccionario)
#Con este le paso como parametro la llave que deseo eliminar junto a su valor
'''diccionario.pop(3)
print(diccionario)'''

#Con este elimino todo el diccionario
'''diccionario.clear()
print(diccionario)'''

#De aqui solamente obtengo el valor de la llave que le pase como parametro
#print(diccionario.get(2))

#Con este solamente agrego a final de la final un nuevo llave:valor
diccionario.setdefault(4, 5)
print(diccionario)

#Con este uno 2 diccionarios para que lo haga de forma ordenada y si se repite en alguno de los 2, se eliminara uno por el otro
diccionario.update(diccionario2)
print(diccionario)

#Aqui se hace una copia del diccionario
diccionario.copy()
print(diccionario)