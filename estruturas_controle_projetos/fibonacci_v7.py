def fibonacci(quantidade):
    lista_fibonacci = [0, 1]

    for _ in range(2, quantidade):  # range(quantidade - 2)
        lista_fibonacci.append(sum(lista_fibonacci[-2:]))

    return lista_fibonacci


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib, end=', ')
