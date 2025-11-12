import math

## Questão 1
def f(x):
    return math.sqrt(x) - math.cos(x)

a = 0
b = 1

for i in range(1, 4):
    p = (a + b) / 2
    fp = f(p)
    
    print(f"Iteração {i}:")
    print(f"  a = {a:.3f}, b = {b:.3f}, p{i} = {p:.3f}, f(p{i}) = {fp:.6f}")
    
    if f(a) * fp < 0:
        b = p
    else:
        a = p

print(f"\nResultado: p3 =", p)

# Questão 2
def f(x):
    return 3*(x+1)*(x-0.5)*(x-1)

a = -2
b = 1.5

for i in range(1, 4):
    p = (a + b) / 2
    fp = f(p)
    
    print(f"Iteração {i}:")
    print(f"  a = {a:.3f}, b = {b:.3f}, p{i} = {p:.3f}, f(p{i}) = {fp:.6f}")
    

    if f(a) * fp < 0:
        b = p
    else:
        a = p

print("\nResultado: p3 =", p)


