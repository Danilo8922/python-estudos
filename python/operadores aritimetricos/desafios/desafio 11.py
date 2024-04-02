altura = float(input('qual é a altura da parede? '))
largura = float(input('qual é a largura da parede? '))
area = altura * largura
tinta = 2
litros_de_tinta = area / 2
latas_de_tinta = int(litros_de_tinta / 18)
print('A area da sua parede é {} metros quadrados para pintar essa parede precisa de {} litros de tinta ou seja {} latas de tinta'.format(area, litros_de_tinta, latas_de_tinta))

 