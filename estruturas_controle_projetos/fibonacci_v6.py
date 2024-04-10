def fibonacci(quantidade):
    lista_fibonacci = [0, 1]

    while True:
        lista_fibonacci.append(sum(lista_fibonacci[-2:]))

        if len(lista_fibonacci) == quantidade:
            break

    return lista_fibonacci


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib, end=', ')
