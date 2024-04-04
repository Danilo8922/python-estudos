import math
catetoP = float(input('qual é o cateto oposto do triangulo '))
catetoA = float(input('qual é o cateto adjacente do triangulo '))
hipotenusa = math.pow(catetoP, 2) +  math.pow(catetoA, 2)
raiz_da_hipotenusa = math.sqrt(hipotenusa)
print('o cateto oposto é {} e o cateto adjacente é {} então a hipotenusa é {:.2f}' .format(catetoP, catetoA, raiz_da_hipotenusa))