def fibonacci(valor):
    if valor <= 1:
        return valor
    else:
        atual, ultimo = 1, 1
        for i in range(2, valor):
            atual, ultimo = atual + ultimo, atual
        return atual


print(fibonacci(int(input('Entre com o valor da sequencia de Fibonacci:'))))
