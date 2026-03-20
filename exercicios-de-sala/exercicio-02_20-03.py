def verificar_potencia(n, b):
    """
    Retorna "0" se "n" não for potência (natural != 0) de "b"
    Retorna "1" se "n" for potência (natural != 0) de "b"
    """

    if n < 1 or b <= 1:
        return 0

    while n % b == 0:
        n /= b

    if n == 1:
        return 1
    
    return 0

def funcao(numero: int):
    """
    F(n) = F(n/2) + 3*n;
    """

    if verificar_potencia(numero, 2) == 0:  # Caso inválido
        return 0

    if numero == 1:     # Critério de parada
        return 5

    return funcao(numero/2) + 3*numero      # Passo recursivo

n = int(input("\nDigite o valor de 'n' (potência de 2): "))
print(f"Resultado de F(n): {funcao(n)}\n")
