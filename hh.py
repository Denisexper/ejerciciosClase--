precio = float(input("ingrese el precio del producto: "))
color = input("ingresa el color de bolita: ")

if color == "azul":
    descunt = precio * 0.5
    finalprice = precio - descunt
    print("porcentaje de descuento es: ",5, "%")
    print("total de descuento: ", descunt)
    print("precio final: ", finalprice)

elif color == "negro":
    descunt = precio * 0
    finalprice = precio - descunt
    print("porcentaje del descuento es: ", 0, "%")
    print("total de descuento:  ", descunt)
    print("precio final: ",finalprice)
    print("tu bolita no tiene descuento")

elif color == "rosada":
    descunt = precio * 0.75
    finalprice = precio - descunt
    print("porcentaje del descuento es: ", 0.75, "%")
    print("total de descuento:  ", descunt)
    print("precio final: ",finalprice)
    
elif color == "roja":
    descunt = precio * 0.15
    finalprice = precio - descunt
    print("porcentaje del descuento es: ", 0.15, "%")
    print("total de descuento:  ", descunt)
    print("precio final: ",finalprice)

else:
    print("tu bola no tiene descuento")
return color

    


    




