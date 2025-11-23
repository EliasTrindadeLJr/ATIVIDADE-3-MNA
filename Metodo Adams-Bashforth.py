import math
print("-"*40)
print("Questão 1")
def f(t, y):
    return y*(math.exp(3*t) - 2)

# Solução exata
def y_exact(t):
    return (1/5)*math.exp(-2*t) + (1/5)*math.exp(3*t)*(t - 1/5)

# Runge–Kutta de 4ª ordem (para iniciar o AB4)
def rk4(f, t, y, h):
    k1 = f(t, y)
    k2 = f(t + h/2, y + h*k1/2)
    k3 = f(t + h/2, y + h*k2/2)
    k4 = f(t + h, y + h*k3)
    return y + h*(k1 + 2*k2 + 2*k3 + k4)/6

# Adams–Bashforth 4ª ordem
def adams_bashforth_4(f, t0, y0, h, n):
    t = [t0 + i*h for i in range(n+1)]
    y = [0]*(n+1)

    # Valores iniciais
    y[0] = y0

    # Usa RK4 para gerar y1, y2, y3
    for i in range(3):
        y[i+1] = rk4(f, t[i], y[i], h)

    # Adams–Bashforth 4ª ordem
    for i in range(3, n):
        y[i+1] = y[i] + h*(55*f(t[i],y[i])
                           - 59*f(t[i-1],y[i-1])
                           + 37*f(t[i-2],y[i-2])
                           - 9*f(t[i-3],y[i-3]))/24

    return t, y

# Parâmetros
h = 0.2
t0 = 0
y0 = 0.5
n = 10

# Executa o método
t, y_ab4 = adams_bashforth_4(f, t0, y0, h, n)

# Imprime tabela
print(f"{'t_i':<5} {'AB4':<15} {'Erro':<15}")
for i in range(n+1):
    y_ex = y_exact(t[i])
    print(f"{t[i]:<5.1f} {y_ab4[i]:<15.7f} {abs(y_ab4[i]-y_ex):.7f}")

#-----------------------------------------
#Questão 2
print("-"*40)
print("Questão 2")
def f(t, y):
    return 1+ (t - y)**2

# Solução exata
def y_exact(t):
    return 2*t+1/(1-t)

# Runge–Kutta de 4ª ordem (para iniciar o AB4)
def rk4(f, t, y, h):
    k1 = f(t, y)
    k2 = f(t + h/2, y + h*k1/2)
    k3 = f(t + h/2, y + h*k2/2)
    k4 = f(t + h, y + h*k3)
    return y + h*(k1 + 2*k2 + 2*k3 + k4)/6

# Adams–Bashforth 4ª ordem
def adams_bashforth_4(f, t0, y0, h, n):
    t = [t0 + i*h for i in range(n+1)]
    y = [0]*(n+1)

    # Valores iniciais
    y[0] = y0

    # Usa RK4 para gerar y1, y2, y3
    for i in range(3):
        y[i+1] = rk4(f, t[i], y[i], h)

    # Adams–Bashforth 4ª ordem
    for i in range(3, n):
        y[i+1] = y[i] + h*(55*f(t[i],y[i])
                           - 59*f(t[i-1],y[i-1])
                           + 37*f(t[i-2],y[i-2])
                           - 9*f(t[i-3],y[i-3]))/24

    return t, y

# Parâmetros
h = 0.5
t0 = 2
y0 = 1
n = 4

# Executa o método
t, y_ab4 = adams_bashforth_4(f, t0, y0, h, n)

# Imprime tabela
print(f"{'t_i':<5} {'AB4':<15} {'Erro':<15}")
for i in range(n+1):
    y_ex = y_exact(t[i])
    print(f"{t[i]:<5.1f} {y_ab4[i]:<15.7f} {abs(y_ab4[i]-y_ex):.7f}")
