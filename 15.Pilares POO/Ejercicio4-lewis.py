#Quiero un metodo que me indique si una palabra es palindromo 
#El metodo debe retornar tru si es palindromo y false si es lo contrario
def palindroma(palabra):
    
    lista = []
    cadenaRevertida = ""

    for i in palabra:
        lista.append(i)

#No puedes hacer operaciones con diferentes tipos de datos, tuplas con tuplas, listas con listas
#Si no puedes usarlas, las debes de convertir en las que necesitas para su uso correcto

    lista.reverse()
    for i in lista:
        cadenaRevertida += i

    if palabra == cadenaRevertida:
        print("True")
    else:
        print("False")

palindroma("oro")

