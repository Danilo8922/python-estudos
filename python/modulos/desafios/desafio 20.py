from random import shuffle
n1 = str(input('digite um nome '))
n2 = str(input('digite outro nome '))
n3 = str(input('digite mais um nome ')) 
n4 =  str(input('digite o ultimo nome '))
nomes = [n1, n2, n3, n4 ]
ordem_dos_trabalhos = shuffle(nomes)
print('odem  de quem vai apresentar os trabalhos primeiro')
print(nomes)