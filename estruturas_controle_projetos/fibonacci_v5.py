def fibonacci(limite):
    lista_fibonacci = [0, 1]

    while lista_fibonacci[-1] < limite:
        lista_fibonacci.append(sum(lista_fibonacci[-2:]))

    return lista_fibonacci


if __name__ == '__main__':
    for fib in fibonacci(1000):
        print(fib, end=', ')
