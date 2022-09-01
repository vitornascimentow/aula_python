area_pintada = float(input('Informe o tamanho da área em m²:'))

quantidade_litro = area_pintada / 3
quantidade_lata = quantidade_litro / 18
latas_arredondada = round(quantidade_lata + .5)
valor = latas_arredondada * 80 

print('Latas de tintas: ', round(latas_arredondada, 2))
print('Preço total: ', valor)


