mb = int(input("Digite o valor gasto com Material Básico: "))
ma = int(input("Digite o valor gasto com Material de Acabamento: "))
maoObra = (mb + ma) * 1.4
valorTotal = mb + ma + maoObra

print('Valor da obra: ', maoObra, 'Valor Total da Obra: ', valorTotal)