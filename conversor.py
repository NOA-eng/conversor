
pesos = input("Cuantos pesos tienes?:  ")
pesos = float(pesos)



# dolares
valor_dolar = 91.64
impuestoPais = 0.30
recargoGana = 0.35

pago = pesos * impuestoPais
pago2 = pesos * recargoGana

pesos = pago + pago2

dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)

print('Tienes $'+ dolares + " dolares")
