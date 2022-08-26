quantidadeCasas = int(input('Digite a quantidade de casas a serem construídas: '))
tamanhoM2 = int(input('Digite o tamanho em m² de uma casa: '))
precoSacoCimento = int(input('Digite o preço do Saco de Cimento com 50kg: '))

quantidadeTotalConstruidos = quantidadeCasas * tamanhoM2
quantidadeSeremCompradosCimento = quantidadeTotalConstruidos /10
valorGastoCimento = quantidadeSeremCompradosCimento * precoSacoCimento

print("M² a serem construídos: ", quantidadeTotalConstruidos)
print("Quantidade de cimento a serem comprados em sacos: ", quantidadeSeremCompradosCimento)
print("O valor gasto de cimento R$ ", valorGastoCimento)