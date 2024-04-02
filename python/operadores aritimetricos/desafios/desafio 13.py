salario = float(input('qual é o seu salario? '))
acressimo = 15
valor_do_acressimo = salario * 15 / 100
salario_atual = salario + valor_do_acressimo
print('O seu salario atual é de {}R$ vc esta recebendo {}% de acressimo que dá {}R$, então seu salario atual fica {}R$'.format(salario, acressimo, valor_do_acressimo, salario_atual))