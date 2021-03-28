#this is a function?
def conversion(moneda):
    total = moneda * dolar
    total = round(total, 2)
    return total


# this is a Option?
menu = """ 
Bienvenidos a tu conversor de divisas 

1- Pesos Argentinos
2- Soles Peruanos
3- Dolar Canadiense

Elige una opccion: """

option = int(input(menu))
dolar = float(input("Cuantos dolares quieres comprar?: "))


#this is a conditional?
if option == 1:
    #impuestos
    pesoArg = 91.64
    impuestoPais = 0.30
    ganaArg = 0.35
    p = pesoArg * impuestoPais
    p2 = pesoArg * ganaArg
    pesoArg += p + p2
    pesoArg = round(pesoArg, 2)
    final = conversion(pesoArg)
    dolar = str(dolar)
    final = str(final)
    print(dolar + " dolares es $" + final + "pesos")

elif option == 2:
    solPer = 3.79
    final = conversion(solPer)
    final = round(final, 2)
    final = str(final)
    dolar = str(dolar) 
    print(dolar + " dolares es $" + final + "soles")

elif option == 3:
    dolarCanad = 1.26
    final = conversion(dolarCanad)
    final = round(final)
    final = str(final)
    dolar = str(dolar)
    print(dolar + " dolares es $" + final + " dolares canadienses")




















