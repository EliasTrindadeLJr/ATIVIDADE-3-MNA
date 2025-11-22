import math
print("Questão 1:")
def midpoint_method(f, a, b, N, alpha):
    h = (b - a) / N
    t = a
    w = alpha
    print(f"Passo 0: t = {t}, w = {w}")

    for i in range(1, N + 1):
        k1 = f(t, w)
        k2 = f(t + h/2, w + (h/2)*k1)
        w = w + h * k2
        t = a + i * h
        print(f"Passo {i}: t = {t}, w = {w}")

    return w

def f(t, y):
    return t * math.exp(3*t) - 2*y  

a, b = 0, 1
alpha = 0
N = 2  
resultado = midpoint_method(f, a, b, N, alpha)
print(f"\nAproximação final: y(1) ≈ {resultado}")
print("-" * 40)

#Questao 2

print("\nQuestão 2:")

def midpoint_method(f, a, b, N, alpha):
    h = (b - a) / N
    t = a
    w = alpha
    print(f"Passo 0: t = {t}, w = {w}")

    for i in range(1, N + 1):
        k1 = f(t, w)
        k2 = f(t + h/2, w + (h/2)*k1)
        w = w + h * k2
        t = a + i * h
        print(f"Passo {i}: t = {t}, w = {w}")

    return w

def f(t, y):
    return 1+(t - alpha)**2 

a, b = 2, 3
alpha = 1
N = 2  
resultado = midpoint_method(f, a, b, N, alpha)
print(f"\nAproximação final: y(1) ≈ {resultado}")
