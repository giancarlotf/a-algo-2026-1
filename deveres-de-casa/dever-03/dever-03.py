def verifica_palindromo(array: list, i=0, j=None):
    """
    Retorna "0" se o array não for um palíndromo
    Retorna "1" se o array for um palíndromo
    """

    # Define o último índice do array
    if j is None:
        j = len(array) - 1

    # Critério de parada
    if i >= j:
        return 1

    # Verificação / Condição de falha
    if array[i] != array[j]:
        return 0

    # Passo recursivo
    return verifica_palindromo(array, i+1, j-1)

# Teste
arrays = {
    "array1": [0, 1, 2, 3, 2, 1, 0],            # É palíndromo
    "array2": ["a", "b", "b", "a"],             # É palíndromo
    "array3": ["a", "b", "c", "b", "a"],        # É palíndromo
    "array4": ["a", "b", "c", "f", "b", "a"],   # Não é palíndromo

    "array5": [],       # É palíndromo
    "array6": [0],      # É palíndromo
    "array7": [0, 1]    # Não é palíndromo
}

for nome, array in arrays.items():
    print(f"{nome}: {verifica_palindromo(array)}")