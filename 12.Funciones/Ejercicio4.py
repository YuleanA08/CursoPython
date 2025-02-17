#Ejercicio 4
#Escribir una función que calcule el total de una factura tras aplicarle
#el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de
#IVA a aplicar, y devolver el total de la factura. Si se invoca la función
#sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

compras = []
numDeCompras = int(input("Cuantas compras vas a registrar:"))
def factura():
    for i in range(0,numDeCompras):
        precios = int(input("Ingrese el valor de la compra:"))
        compras.append(precios)
    pregunta = input("¿Sabe usted el valor del IVA?:")
    if pregunta == "si":
        ivaAplicar= int(input("Ingrese IVA a aplicar en el producto:"))
        total = sum(compras) * (ivaAplicar/100)
    else:
        total = sum(compras) * (0.21)
    return total

print(factura())