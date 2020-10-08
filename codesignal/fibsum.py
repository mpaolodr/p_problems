def fibonacciSimpleSum2(n):

    if n == 1:

        return True

    if n == 0:

        return False

    reference = dict_gen(n)

    for key in reference:

        if key <= n:

            if n - key in reference:

                return True

        else:

            break

    return False


def fibo(n, cache=None):

    if cache is None:

        cache = dict()

    if n in cache:

        return cache[n]

    else:

        if n == 0:

            return 0

        if n == 1:

            return 1

        value = fibo(n - 1, cache) + fibo(n - 2, cache)
        cache[n] = value

        return cache[n]


def dict_gen(n):

    memory = dict()

    for num in range(n + 1):

        memory[fibo(num)] = None

    return memory
