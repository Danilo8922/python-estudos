import math

angulo = int(input('digite um angulo '))
anguloC = math.radians(angulo)
seno = math.sin(anguloC)
coseno = math.cos(anguloC)
tangente = math.tan(anguloC)
print(' o seno de {}° é {:.2f}, O coseno de {}° é {:.2f}, E a tangente de {}° é {:.2f}' .format(angulo, seno, angulo, coseno, angulo, tangente) )