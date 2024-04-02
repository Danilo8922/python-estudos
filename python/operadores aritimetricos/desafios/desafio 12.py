valor_do_produto = float(input('qual é o valor do produto ? '))
porcento = 5
desconto = (valor_do_produto * porcento) / 100
valor_com_desconto = valor_do_produto - desconto
print('o produto esta custando {}R$ com {}% de desconto, o valor do desconto é {} então vc vai pagar {}R$' .format(valor_do_produto, porcento, desconto, valor_com_desconto))