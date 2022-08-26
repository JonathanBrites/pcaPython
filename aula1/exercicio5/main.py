qpessoas = int(input('Quantidade de Pessoas que bebem café: '))
precoCafe = int(input('Preço do Kg do Café: '))

prodCafe = qpessoas * 0.200 
kgCafeComprado = (qpessoas * 0.200) /5
vlCafe = kgCafeComprado * precoCafe


print('A quantidade de litros de café que devem ser produzidos é: ', prodCafe, 'Litros.')
print('A quantidade de Kg de Café que devem ser comprados é: ', kgCafeComprado, 'kg')
print('O valor total gasto de café é: ', vlCafe)

