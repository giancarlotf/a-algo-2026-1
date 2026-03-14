def substring(string: str, inicio=0, fim=1):
    if inicio > len(string):                            # Critério de parada
        return

    if fim > len(string):                               # 1º Passo recursivo
        return substring(string, inicio+1, inicio+2)

    print(string[inicio:fim])

    return substring(string, inicio, fim+1)             # 2º Passo recursivo

string = "Texto"
substring(string)