while True:
    try:
        edad = int (input("Ingresa tu edad:"))
        print("Tu edad es:", edad)
        break
    except:
        print("Ingresaste un valor erroneo")
    finally:
        print("La ejecucion a finalizado")