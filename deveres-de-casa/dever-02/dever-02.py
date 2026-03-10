from sys import setrecursionlimit
from time import perf_counter

setrecursionlimit(1002)     # Profundidade de recursão alterada (1000 -> 1002) por causa de n = 1000

def fatorial(numero: int):
    if numero < 0:                          # Caso inválido
        return -1
    if numero <= 1:                         # Critério de parada
        return 1
    return fatorial(numero - 1) * numero    # Passo recursivo

n = [10, 100, 500, 1000]

for numero in n:                    # Laço de repetição para percorrer os números da lista "n"
    inicio = perf_counter()
    resultado = fatorial(numero)    # Aplicação dos números de "n" no algoritmo
    fim = perf_counter()
    tempo = fim - inicio            # Cálculo do tempo de execução da função "fatorial()"

    print(f"Tempo de execução para n = {numero}: {tempo: .16f}")
    print(f"Resultado: {numero}! = {resultado}\n")
