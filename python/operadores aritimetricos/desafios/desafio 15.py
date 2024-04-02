km_percorrido = float(input('Quantos Km foi percorrido pelo carro? '))
dias_alugados = int(input('Por quantos dias ele foi alugado? '))
aluguel = int(60)
preço_por_km_percorrido = float(0.15)
pagar_km_percorrido = km_percorrido * preço_por_km_percorrido
pagar_dias_alugados = dias_alugados * aluguel
total_a_pagar = pagar_km_percorrido + pagar_dias_alugados
print('vc percorreu {}Km e ficou {} dias com o carro')
print('o aluguel é {} e a tacha dos km percrridos é {}')
print('o valor do aluguel é {} e atacha dos km percrrido ficou {}' )
print('o total a pagar é {}')