#variaveis
dias_alugados = int(input('Por quantos dias ele foi alugado? '))
km_percorrido = float(input('Quantos Km foi percorrido pelo carro? '))
aluguel = int(60)
preço_por_km_percorrido = float(0.15)
pagar_km_percorrido = km_percorrido * preço_por_km_percorrido
pagar_dias_alugados = dias_alugados * aluguel
total_a_pagar = pagar_km_percorrido + pagar_dias_alugados
#programa funcionando 
print('Você ficou {} dias com o carro e você percorreu {}Km' .format(km_percorrido, dias_alugados))
print('A diaria do carro é R${} e a taxa dos km percrridos é R${}' .format(aluguel, preço_por_km_percorrido ))
print('o valor do aluguel é R${:.2f} e a taxa dos km percrrido ficou R${}'.format(pagar_dias_alugados, pagar_km_percorrido))
print('o total a pagar do aluguel é R${}' .format(total_a_pagar))