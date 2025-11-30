import math

print("-"*40)
print("Questão 1")

def newton_method(f, df, p0, TOL, N0):
    i = 1
    while i <= N0:
        p = p0 - f(p0) / df(p0)
        print(f"Iteração {i}: p = {p}")
        if abs(p - p0) < TOL:
            print(f"\nConvergência atingida após {i} iterações.")
            return p
        i += 1
        p0 = p

    print("\nO método falhou após", N0, "iterações.")
    return None

#Função e derivada
def f(x):
    return x**3 - 2*x**2 - 5

def df(x):
    return 3*x**2 - 4*x


# Parâmetros iniciais

#valores de p0 podem ser digitados aqui em a e b se desejar ou so substituidos neles mesmo
a = 1
b = 4
p0 =  a+b / 4  #Ponto Medio  
TOL = 1e-4     #Tolerancia do Erro
N0 = 5         # Iteraçoes   

raiz = newton_method(f, df, p0, TOL, N0)
if raiz is not None:
    print(f"\nA raiz aproximada é: {raiz:.10f}")

print("-"*40)
print("Questão 2")
def newton_method(f, df, p0, TOL, N0):
    i = 1
    while i <= N0:
        p = p0 - f(p0) / df(p0)
        print(f"Iteração {i}: p = {p}")
        if abs(p - p0) < TOL:
            print(f"\nConvergência atingida após {i} iterações.")
            return p
        i += 1
        p0 = p

    print("\nO método falhou após", N0, "iterações.")
    return None

#Função e derivada
def f(x):
    return x**3+3*x**2-1

def df(x):
    return 3*x**2 + 6 * x


# Parâmetros iniciais

#valores de p0 podem ser digitados aqui em a e b se desejar ou so substituidos neles mesmo
a = -3
b = -2
p0 =  a+b / 4     
TOL = 1e-4     
N0 = 5             

raiz = newton_method(f, df, p0, TOL, N0)
if raiz is not None:
    print(f"\nA raiz aproximada é: {raiz:.10f}")

