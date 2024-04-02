n1 = float(input('quantos reais vc tem na conta? '))
dollars_em_reais = 5.06
dollars_comprados = n1 / dollars_em_reais
print('vc tem na carteira {}R$ o dollar hje em 2024 está {}$ então vc pode obter {:.3f}$' .format(n1, dollars_em_reais, dollars_comprados))