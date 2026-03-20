from sys import setrecursionlimit

def funcao_01(n: int):
    """
    F(n) = F(n - 1) + n + 1
    """

    if n == 0:      # Critério de parada
        return 1

    return funcao_01(n - 1) + n + 1     # Passo recursivo

def funcao_02(n: int):
    """
    F(n) = F(n - 1) + 3*n + 2
    """

    if n == 1:      # Critério de parada
        return 1

    return funcao_02(n - 1) + 3*n + 2   # Passo recursivo

limite = int(input("\nDigite o valor do limite de recursão (Padrão = 1000): "))
setrecursionlimit(limite)     # Mudança da profundidade de recursão, para testar valores mais altos

n = int(input("\nDigite o valor de 'n': "))
print("\nFunção 1:\n\t", funcao_01(n), "\nFunção 2:\n\t", funcao_02(n))
