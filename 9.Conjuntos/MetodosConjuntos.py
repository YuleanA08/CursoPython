#Los conjuntos no muentras datos repetidos
conjunto1 = {1,1,2,2,3,3,4,4,5}
lista = [1,2,3,4,5]
#######################################################
conjunto = {1,2,3,4,5}

conjunto.add(20)
print(lista)
#Con estos se puede eliminar un dato del conjunto, se pasa como parametro lo que se desea eliminar
conjunto.remove(1)
print(lista)
conjunto.discard(1)
print(lista)
#Pop en estos casos toma cualquiera de los datos y lo elimina
conjunto.pop()
print(conjunto)
#Permite añadir componentes iterables
conjunto.update([1,2,3])
print(conjunto)
#Este permite limpiar todos los datos dentro del conjunto
conjunto.clear()
print(conjunto)