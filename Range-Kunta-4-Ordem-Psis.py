import math
import numpy as np

print("-"*40)
# Sistema de equações
def f(t, u, v):
    du = 3*u + 2*v - (2*t**2 + 1)*math.exp(2*t)
    dv = 4*u + v + (t**2 + 2*t - 4)*math.exp(2*t)
    return du, dv

# Parâmetros
t0 = 0
tf = 1
h = 0.2
n = int((tf - t0) / h)

# Condições iniciais
u = 1.0
v = 1.0

# Arrays para armazenar resultados
t_values = np.linspace(t0, tf, n+1)
u_values = np.zeros(n+1)
v_values = np.zeros(n+1)

u_values[0] = u
v_values[0] = v

# Método de Runge-Kutta 4ª ordem
for i in range(n):
    t = t_values[i]

    k1_u, k1_v = f(t, u, v)
    k1_u *= h
    k1_v *= h

    k2_u, k2_v = f(t + h/2, u + k1_u/2, v + k1_v/2)
    k2_u *= h
    k2_v *= h

    k3_u, k3_v = f(t + h/2, u + k2_u/2, v + k2_v/2)
    k3_u *= h
    k3_v *= h

    k4_u, k4_v = f(t + h, u + k3_u, v + k3_v)
    k4_u *= h
    k4_v *= h

    u += (k1_u + 2*k2_u + 2*k3_u + k4_u) / 6
    v += (k1_v + 2*k2_v + 2*k3_v + k4_v) / 6

    u_values[i+1] = u
    v_values[i+1] = v

# Impressão da tabela
print("Tabela de Resultados - Questão 1")
print("-"*40)
print("i     t         u_aprox       v_aprox")
print("-" * 50)
for i in range(n+1):
    print(f"{i:2}   {t_values[i]:.1f}   {u_values[i]:.10f}   {v_values[i]:.10f}")


#questão2 

print("-"*40)

import math
import numpy as np

# Transformando a EDO de 2ª ordem em sistema de 1ª ordem:
# y1 = y, y2 = y'
# y1' = y2
# y2' = y'' = 2*y2 - y1 + t*exp(t) - t
def f(t, y1, y2):
    dy1 = y2
    dy2 = 2*y2 - y1 + t*math.exp(t) - t
    return dy1, dy2

# Parâmetros
t0 = 0
tf = 1
h = 0.1
n = int((tf - t0) / h)

# Condições iniciais
y1 = 0.0  # y(0)
y2 = 0.0  # y'(0)

# Arrays para armazenar resultados
t_values = np.linspace(t0, tf, n+1)
y1_values = np.zeros(n+1)
y2_values = np.zeros(n+1)

y1_values[0] = y1
y2_values[0] = y2

# Método de Runge-Kutta 4ª ordem
for i in range(n):
    t = t_values[i]

    k1_y1, k1_y2 = f(t, y1, y2)
    k1_y1 *= h
    k1_y2 *= h

    k2_y1, k2_y2 = f(t + h/2, y1 + k1_y1/2, y2 + k1_y2/2)
    k2_y1 *= h
    k2_y2 *= h

    k3_y1, k3_y2 = f(t + h/2, y1 + k2_y1/2, y2 + k2_y2/2)
    k3_y1 *= h
    k3_y2 *= h

    k4_y1, k4_y2 = f(t + h, y1 + k3_y1, y2 + k3_y2)
    k4_y1 *= h
    k4_y2 *= h

    y1 += (k1_y1 + 2*k2_y1 + 2*k3_y1 + k4_y1) / 6
    y2 += (k1_y2 + 2*k2_y2 + 2*k3_y2 + k4_y2) / 6

    y1_values[i+1] = y1
    y2_values[i+1] = y2

# Solução exata
def y_exact(t):
    return (1/6)*t**3*math.exp(t) - t*math.exp(t) + 2*math.exp(t) - t - 2

# Impressão da tabela
print("Tabela de Resultados - Questão 2")
print("-"*40)

print("i     t         y_aprox       y_exato       erro")
print("-" * 60)
for i in range(n+1):
    y_ex = y_exact(t_values[i])
    erro = abs(y1_values[i] - y_ex)
    print(f"{i:2}   {t_values[i]:.1f}   {y1_values[i]:.10f}   {y_ex:.10f}   {erro:.10f}")
