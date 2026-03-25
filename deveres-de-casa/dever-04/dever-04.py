"""
Desenvolvimento da fórmula fechada

F(n) = {2, n = 1
       {2*F(n-1) + 2*n, n > 1

F(n) = 2*n + 2(2(n-1) + 2(2(n-2) + 2(...)))
F(n) = 2*n + (n-1)*2^2 + (n-2)*2^3 + ... + 3*2^{n-2} + 2*2^{n-1} + 2^n

F(n) = sum_{k=0}^{n-1} (n-k)*2^{k+1}
F(n) = sum_{k=0}^{n-1}(n*2*2^k) - sum_{k=0}^{n-1}(k*2*2^k)
F(n) = 2*n * sum_{k=0}^{n-1}(2^k) - 2 * sum_{k=0}^{n-1}(k*2^k)

F(n) = 2*n*(2^n - 1) - 2*((n-2)*2^n + 2)
F(n) = 4*2^n - 2n - 4
F(n) = 2^{n+2} - 2*(n+2)
"""

from sys import setrecursionlimit
from time import perf_counter

def funcao_recursiva(n: int):
    """
    F(n) = 2*F(n-1) + 2*n
    """

    if n < 1:       # Caso inválido
        print("'n' deve ser maior que 0")
        return -1

    if n == 1:      # Caso base
        return 2

    return 2*funcao_recursiva(n-1) + 2*n    # Passo recursivo

limite = int(input("\nDigite o valor do limite de recursão (Padrão = 1000): "))
if limite < 1000: limite = 1000
setrecursionlimit(limite)     # Mudança da profundidade de recursão, para testar valores mais altos

n = int(input("\nDigite um valor inteiro 'n' >= 1: "))

inicio_01 = perf_counter()
resultado_01 = funcao_recursiva(n)
fim_01 = perf_counter()
delta_01 = fim_01 - inicio_01

inicio_02 = perf_counter()
resultado_02 = 2**(n+2) - 2*(n+2)
fim_02 = perf_counter()
delta_02 = fim_02 - inicio_02

print(f"\nResultado: {resultado_01}")
print(f"Tempo de execução:\n\tFunção recursiva: {delta_01}\n\tFórmula fechada:  {delta_02}\n")