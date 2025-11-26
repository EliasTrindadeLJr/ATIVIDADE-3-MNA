import numpy as np
import math
#questão 1
a=0
b= 1
n= 2
CondInicial=0

h=(b-a)/n

t=a
w=CondInicial

#math.exp = exponencal
def f(t, w):
    return t * math.exp(3*t) - 2*w
print(f"Questão 1:")
print(f"t = {t}, w = {w}")

for i in range(1, n+1):
    k1=h*f(t, w)
    k2=h*f(t + h/2, w + k1/2)
    k3=h*f(t + h/2, w + k2/2)
    k4=h*f(t + h, w + k3)
    
    w=w+(k1 + 2*k2 + 2*k3 + k4)/6
    t=a+i*h

    print(f"t = {t}, w = {w:.13f}")

print("-"*30)

#questão 2

a= 2
b= 3
n= 2
CondInicial=1

h=(b-a)/n

t=a
w=CondInicial

#math.exp = exponencal
def f(t, w):
    return 1+(t - w)**2

print(f"Questão 2:")
print(f"t = {t}, w = {w}")

for i in range(1, n+1):
    k1=h*f(t, w)
    k2=h*f(t + h/2, w + k1/2)
    k3=h*f(t + h/2, w + k2/2)
    k4=h*f(t + h, w + k3)
    
    w=w+(k1 + 2*k2 + 2*k3 + k4)/6
    t=a+i*h

    print(f"t = {t}, w = {w:.13f}")
