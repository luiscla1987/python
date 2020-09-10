def fibonacci(valor):
    if valor <= 1:
        return valor
    else:
        return fibonacci(valor - 1) + fibonacci(valor - 2)


print(fibonacci(int(input('Entre com o valor da sequencia de Fibonacci:'))))
