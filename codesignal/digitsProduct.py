def digitsProduct(product):

    num = 1

    while num <= 100000:

        num_split = list(str(num))

        running_total = 1

        for n in num_split:

            running_total *= int(n)

        if running_total == product:

            return num

        num += 1

    return -1
