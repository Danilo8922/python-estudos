import random
nomes = ['Danilo', 'Perola', 'João', 'Ana' ]
ordem_dos_trabalhos = random.shuffle(nomes)
print('odem  de quem vai apresentar os trabalhos primeiro')
for nome in nomes:
  print(nome)