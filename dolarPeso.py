#opciones de monedas
menu = """
Bienvenido al converso de monedas:

Selecciona las en que moneda queres comprar dolares

1- Pesos argentinos
2- Soles peruanos
3- Dolar canadiense

Elige una opción: """
opcion = int(input(menu))


dolar = input("Cuantos dolares quieres comprar?: ")
dolar = float(dolar)

p = pesoArg * impuestoPais
p2 = pesoArg * ganaArg

#this is a function?
def conversor(moneda, dolar):
    pago = moneda * dolar
    pago = round(pago, 2)
    pago = str(pago)
    return pago

if (opcion == 1):
    pass
elif(opccion == 2):
    pass
elif(opcion == 3)
    pass


#valores
pesoArg = 91.64
impuestoPais = 0.30
ganaArg = 0.35



# pago final en pesos
# pesoArg += p + p2
# pesoArg = round(pesoArg, 2)

# sol peruano
# solPer = 3.79

#operaciones


# pago2 = solPer * dolar
# pago2 = round(pago2, 2)
# pago2 = str(pago2)
# dolar = round(dolar)
# dolar = str (dolar)


# costo final
# print(dolar + ' dolares son $' + pago + ' pesos')
# print(dolar + ' dolares son $' + pago2 + ' soles')












