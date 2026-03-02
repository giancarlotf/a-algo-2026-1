# A barreira do n^2
from random import randint
from time import perf_counter

def insertion_sort(vetor, tamanho):
    for i in range(0, tamanho - 1):
        j = i + 1
        aux = vetor[j]
        while j and vetor[j - 1] > aux:
            vetor[j] = vetor[j - 1]
            j -=1

        vetor[j] = aux

n = [1000, 5000, 10000, 20000, 50000]

for i in range(len(n)):
    lista_1 = [randint(1, n[i]) for _ in range(n[i])]
    lista_2 = lista_1.copy()

    start_1 = perf_counter()
    insertion_sort(lista_1, n[i])
    end_1 = perf_counter()
    delta_1 = end_1 - start_1

    start_2 = perf_counter()
    lista_2 = sorted(lista_2)
    end_2 = perf_counter()
    delta_2 = end_2 - start_2

    print(f"Tempo de execução para a lista de tamanho: {n[i]}")
    print(f"\tinsertion_sort() : {delta_1: .16f}")
    print(f"\tsorted()         : {delta_2: .16f}")
    if delta_1 < delta_2:
        print(f"Resultado: insertion_sort() é {delta_2/delta_1: .4f}X mais rápido\n")
    elif delta_1 > delta_2:
        print(f"Resultado: sorted() é {delta_1/delta_2: .4f}X mais rápido\n")
    else:
        print("Resultado: Empate\n")
