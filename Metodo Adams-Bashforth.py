import math
print("-"*40)
print("Questão 1")

def f1(t, y):
    return t*math.exp(3*t) - 2*y

def y_exact1(t):
    return (1/5)*t*math.exp(3*t) - (1/25)*math.exp(3*t) + (1/25)*math.exp(-2*t)

# Runge–Kutta de 4ª ordem
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

    # Usa RK4 
    for i in range(min(3, n)): 
        y[i+1] = rk4(f, t[i], y[i], h)

    # Adams–Bashforth 4ª ordem 
    for i in range(3, n):
        y[i+1] = y[i] + h*(55*f(t[i],y[i])
                           - 59*f(t[i-1],y[i-1])
                           + 37*f(t[i-2],y[i-2])
                           - 9*f(t[i-3],y[i-3]))/24

    return t, y

# Parâmetros Questão 1
h = 0.2
t0 = 0
y0 = 0
n = 10

# Executa o método
t, y_ab4 = adams_bashforth_4(f1, t0, y0, h, n)

# Imprime tabela
print(f"{'t_i':<5} {'AB4':<15} {'Exata':<15} {'Erro':<15}")
for i in range(n+1):
    y_ex = y_exact1(t[i])
    print(f"{t[i]:<5.1f} {y_ab4[i]:<15.7f} {y_ex:<15.7f} {abs(y_ab4[i]-y_ex):.7f}")

#-----------------------------------------
#Questão 2
print("-"*40)
print("Questão 2")

def f2(t, y):
    return 1 + (t - y)**2

# Solução exata 
def y_exact2(t):
    return t + 1/(1 - t)

# Parâmetros Questão 2 
t0 = 2
y0 = 1
n = 5 

# Executa o método
t, y_ab4 = adams_bashforth_4(f2, t0, y0, h, n)

# Imprime tabela
print(f"{'t_i':<5} {'AB4':<15} {'Exata':<15} {'Erro':<15}")
for i in range(n+1):
    y_ex = y_exact2(t[i])
    print(f"{t[i]:<5.1f} {y_ab4[i]:<15.7f} {y_ex:<15.7f} {abs(y_ab4[i]-y_ex):.7f}")
