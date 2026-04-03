# Analisador de Complexidade com Teorema Mestre
# T(n) = aT(n/b) + f(n)

from math import log

def analisar_complexidade(a: int, b: int, k: int, p: int):
    if a < 1:
        print("(a) deve ser maior ou igual a 1")
        return 0
    if b <= 1:
        print("(b) deve ser maior que 1")
        return 0

    c = log(a, b)

    # f(n) ? n^log_b(a)
    # n^k * log^p(n) ? n^c

    # Comparação entre os expoentes "k" e "c"
    if k < c:
        print("\nCaso do Teorema Mestre: 1")
        print(f"f(n) < n^{c:.4f}")
        print(f"T(n) = Theta(n^{c:.4f})\n")
        return 1
    if k == c:
        # Fator de desempate: log^p(n)
        if p < 0:
            print("\nCaso do Teorema Mestre: 1")
            print(f"f(n) = n^{c:.4f}")
            print(f"T(n) = Theta(n^{c:.4f})\n")
            return 1
        if p >= 0:
            print("\nCaso do Teorema Mestre: 2")
            print(f"f(n) = n^{c:.4f}")
            print(f"T(n) = Theta(n^{c:.4f} * log_{b}(n))\n")
            return 2
    if k > c:
        print("\nCaso do Teorema Mestre: 3")
        print(f"f(n) > n^{c:.4f}")
        print(f"T(n) = Theta(n^{k} * log^{p}(n))\n")
        return 3

print('''\nTeorema Mestre:
        T(n) = aT(n/b) + f(n)
        a: quantidade de subproblemas
        b: tamanho do subproblema
        f(n): tempo dos subproblemas
        f(n) = n^k * log^p(n)\n''')

a = int(input("Digite o valor de 'a': "))
b = int(input("Digite o valor de 'b': "))
k = int(input("Digite o valor de 'k': "))
p = int(input("Digite o valor de 'p': "))

analisar_complexidade(a, b, k, p)
