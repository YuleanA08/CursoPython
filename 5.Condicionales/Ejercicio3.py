palabra1= input("Ingresa una palabra: ")
palabra2= input("Ingresa otra palabra: ")


if len(palabra1)< 3 and len(palabra2) < 3:
    print("NO rima, porque tiene menos de 3 caracteres")
elif palabra1 [-3] == palabra2 [-3: ]:
    print("Hiciste una rima")
elif palabra1[-2] == palabra2 [-2: ]:
    print("Riman un poco")
else:
    print("No rimaste")