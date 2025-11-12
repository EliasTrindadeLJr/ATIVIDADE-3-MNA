import math

def euler_method(f, a, b, N, alpha):

    h = (b - a) / N
    t = a
    w = alpha

    print(f"Passo 0: t = {t:.2f}, w = {w:.6f}")

    for i in range(1, N + 1):
        w = w + h * f(t, w)   
        t = a + i * h        
        print(f"Passo {i}: t = {t:.2f}, w = {w:.6f}")

    return w



def f(t, y):
    return t * math.exp(3 * t) - 2 * y

a = 0      
b = 1      
ci = 0  #  y(0)=0
h = 0.5
N = int((b - a) / h)


resultado = euler_method(f, a, b, N, ci)
print(f"\nAproximação final: y(1) ≈ {resultado:.6f}")
