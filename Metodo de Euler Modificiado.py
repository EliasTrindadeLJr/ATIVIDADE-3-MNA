import numpy as np

def euler_modificado(f, t0, y0, h, n):
    t = np.zeros(n+1)
    y = np.zeros(n+1)
    t[0] = t0
    y[0] = y0
    
    for i in range(n):
        t[i+1] = t[i] + h
        # Preditor (Euler explícito)
        y_pred = y[i] + h * f(t[i], y[i])
        # Corretor (Heun)
        y[i+1] = y[i] + (h/2) * (f(t[i], y[i]) + f(t[i+1], y_pred))
    
    return t, y

print("=== PROBLEMA a) ===")
def f_a(t, y):
    return t * np.exp(3*t) - 2*y

def solucao_a(t):
    return (1/5)*t*np.exp(3*t) - (1/25)*np.exp(3*t) + (1/25)*np.exp(-2*t)

t0_a = 0
y0_a = 0
h_a = 0.5
t_final_a = 1
n_a = int((t_final_a - t0_a) / h_a)

print(f"n_a = {n_a}")  # Debug

t_a, y_a = euler_modificado(f_a, t0_a, y0_a, h_a, n_a)

print("t\t\tEuler Modificado\tSolução Real\t\tErro")
for i in range(len(t_a)):
    y_real = solucao_a(t_a[i])
    erro = abs(y_a[i] - y_real)
    print(f"{t_a[i]:.1f}\t\t{y_a[i]:.8f}\t\t{y_real:.8f}\t\t{erro:.8f}")


# PROBLEMA b)
print("\n=== PROBLEMA b) ===")
def f_b(t, y):
    return 1 + (t - y)**2

def solucao_b(t):
    return t + 1/(1-t)  

t0_b = 2
y0_b = 1
h_b = 0.5
t_final_b = 3
n_b = int((t_final_b - t0_b) / h_b)

print(f"n_b = {n_b}")  

t_b, y_b = euler_modificado(f_b, t0_b, y0_b, h_b, n_b)

print("t\t\tEuler Modificado\tSolução Real\t\tErro")
for i in range(len(t_b)):
    y_real = solucao_b(t_b[i])
    erro = abs(y_b[i] - y_real)
    print(f"{t_b[i]:.1f}\t\t{y_b[i]:.8f}\t\t{y_real:.8f}\t\t{erro:.8f}")

