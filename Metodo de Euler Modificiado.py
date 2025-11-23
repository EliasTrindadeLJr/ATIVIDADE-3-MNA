import math
print("-"*40)
print("Questão 1 – Euler Modificado")

# Questão 1
def f1(t, y):
    return y*(math.exp(3*t) - 2)

# Solução exata Questão 1
def y_exact_1(t):
    return (1/5)*math.exp(-2*t) + (1/5)*math.exp(3*t)*(t - 1/5)

# Método de Euler Modificado (Heun)
def euler_modificado(f, t0, y0, h, n):
    t = t0
    y = y0
    tabela = [(t, y)]

    for i in range(n):
        y_pred = y + h * f(t, y)
        y = y + (h/2) * (f(t, y) + f(t + h, y_pred))
        t += h
        tabela.append((t, y))

    return tabela

# Parâmetros Questão 1
h = 0.2
t0 = 0
y0 = 0.5
n = 10

# Executa
result1 = euler_modificado(f1, t0, y0, h, n)

print(f"{'t_i':<5} {'Euler Modf.':<15} {'Erro':<10}")
for t, w in result1:
    print(f"{t:<5.1f} {w:<15.7f} {abs(w - y_exact_1(t)):.7f}")


#-----------------------------------------
print("-"*40)
print("Questão 2 – Euler Modificado")

# Questão 2
def f2(t, y):
    return 1 + (t - y)**2

# Solução exata Questão 2
def y_exact_2(t):
    return 2*t + 1/(1 - t)

# Parâmetros Questão 2
h = 0.5
t0 = 2
y0 = 1
n = 2

# Executa
result2 = euler_modificado(f2, t0, y0, h, n)

print(f"{'t_i':<5} {'Euler Modf.':<15} {'Erro':<10}")
for t, w in result2:
    print(f"{t:<5.1f} {w:<15.7f} {abs(w - y_exact_2(t)):.7f}")
