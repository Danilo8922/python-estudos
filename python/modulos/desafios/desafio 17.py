from math import pow, sqrt, hypot
catetoP = float(input('qual é o cateto oposto do triangulo '))
catetoA = float(input('qual é o cateto adjacente do triangulo '))
hipotenusa = hypot(catetoA, catetoP )
print('o cateto oposto é {} e o cateto adjacente é {} então a hipotenusa é {:.2f}' .format(catetoP, catetoA, hipotenusa))