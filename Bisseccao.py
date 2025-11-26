import math

# Questão 1
#Defina funcao
def f(x):
    return math.sqrt(x) - math.cos(x)
#valores
a = 0
b = 1

#para i dentro de 1 e 4 que sao as iteraçoes 
for i in range(1, 4):
    p = (a + b) / 2
    fp = f(p)
    
    print(f"Iteração {i}:")
    print(f"  a = {a:.3f}, b = {b:.3f}, p{i} = {p:.3f}, f(p{i}) = {fp:.6f}")
    
    if f(a) * fp < 0: # caso funcao de a ou b x seja maior que 0 = a se menor b
        b = p
    else:
        a = p

print(f"\nResultado: p3 =", p)

# Questão 2
print("\n Questão2")
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


