dolar = input("Cuantos dolares quieres comprar?: ")
dolar = float(dolar)

#valores
pesoArg = 91.64
impuestoPais = 0.30
ganaArg = 0.35

#impuestos
p = pesoArg * impuestoPais
p2 = pesoArg * ganaArg

#pago final en pesos
pesoArg += p + p2
pesoArg = round(pesoArg, 2)

#sol peruano
solPer = 3.79

#operaciones
pago = pesoArg * dolar
pago = round(pago, 2)
pago = str(pago)

pago2 = solPer * dolar
pago2 = round(pago2, 2)
pago2 = str(pago2)
dolar = round(dolar)
dolar = str (dolar)


#costo final
print(dolar + ' dolares son $' + pago + ' pesos')
print(dolar + ' dolares son $' + pago2 + ' soles')












