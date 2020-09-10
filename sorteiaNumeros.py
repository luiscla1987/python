def sorteia(numeros):
    import random
    retornoJogo = []

    while(len(retornoJogo) < numeros):
        sorteado = random.randint(1, 60)
        if sorteado not in retornoJogo:
            retornoJogo.append(sorteado)
    return retornoJogo


print(sorteia(int(input("Digite a quantidade de números para ser sorteado: "))))
