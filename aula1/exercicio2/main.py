tipoA = int(input('Qual a quantidade de leite A foi vendido ? '))
tipoB = int(input('Qual a quantidade de leite B foi vendido ? '))
tipoC = float(input('Qual a quantidade de leite C foi vendido ? '))

leiteVendidoA = int(tipoA*1)
leiteVendidoB = int(tipoB*2)
leiteVendidoC = float(tipoC*4.5)

arrecadado = float(tipoA*1 + tipoB*2 + tipoC*4.5 )

print('O total de leite A vendido foi de R$ ', leiteVendidoA)
print('O total de leite B vendido foi de R$ ', leiteVendidoB)
print('O total de leite C vendido foi de R$ ', leiteVendidoC)
print('O total de leite vendido foi de R$ ', arrecadado)





