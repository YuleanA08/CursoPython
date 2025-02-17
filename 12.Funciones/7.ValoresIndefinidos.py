def argumento(*num):
    for i in num:
        print(i)
    return type(num)

print(argumento(10, 20, 30, 40, 50))
#Todos los argumentos que yo le pase a la funcion
#Seran almacenados en una tupla