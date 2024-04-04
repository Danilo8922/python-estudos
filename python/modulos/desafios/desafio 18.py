from math import radians, sin, cos, tan  

angulo = int(input('digite um angulo '))
anguloC = radians(angulo)
seno = sin(anguloC)
coseno = cos(anguloC)
tangente = tan(anguloC)
print('O seno de {}° é {:.2f}, O coseno de {}° é {:.2f}, E a tangente de {}° é {:.2f}' .format(angulo, seno, angulo, coseno, angulo, tangente))