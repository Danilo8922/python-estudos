from random import choice
n1 = str(input('digite um nome '))
n2 = str(input('digite outro nome '))
n3 = str(input('digite mais um nome ')) 
n4 =  str(input('digite o ultimo nome '))
nomes = [n1, n2, n3, n4 ]
sorteio = choice(nomes)
print('bom vou sortear alguem para apagar o quadro, {} vc apaga o quadro' .format(sorteio))