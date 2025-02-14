voto= input("Vote por su candidato A, B o C: ")

if voto.upper() == "A":
    print("Usted ha votado por el partido ROJO")
elif voto.upper() == "B":
    print("Usted ha votado por el partido VERDE")
elif voto.upper() == "C":
    print("Usted ha votado por el partido AZUL")
else:
    print("Opción errónea")