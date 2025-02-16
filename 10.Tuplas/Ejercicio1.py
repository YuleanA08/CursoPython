#Ejercicio 1
#Escribir una tupla con los meses del año, luego, pide al usuario un nu
#mero, el que haya ingresado, es el mes que debe mostrar en la tupla
meses = ('Ene', 'Febre', 'Mar', 'Abri', 'May', 'Jun', 'Jul', 'Agost', 'Sept', 'Oct', 'Nov', 'Dic')

print(type(meses))

Nmes=int(input("Ingrese un mes del año en numero: "))
if Nmes >0 and Nmes < len(meses):
    print("El mes que escogiste fue: "+meses[Nmes-1])
else:
    print("Estas ingresando un valor que no corresponde a lo normal")