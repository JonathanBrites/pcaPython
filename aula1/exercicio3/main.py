mb = int(input("Digite o valor gasto com Material Básico R$ "))
ma = int(input("Digite o valor gasto com Material de Acabamento R$ "))
maoObra = (mb + ma) * 1.4
valorTotal = mb + ma + maoObra

print('Valor da mão de obra R$ ', maoObra, 'Valor Total da Obra R$ ', valorTotal)