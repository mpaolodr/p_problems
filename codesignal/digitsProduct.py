# def digitsProduct(product):

#     num = 1

#     while num <= 100000:

#         num_split = list(str(num))

#         running_total = 1

#         for n in num_split:

#             running_total *= int(n)

#         if running_total == product:

#             return num

#         num += 1

#     return -1


def digitsProduct(p):

    if p == 0:

        return 10

    elif p == 1:

        return 1

    result = list()

    while p > 1:

        for num in range(9, 1, -1):

            if p % num == 0:

                p /= num

                result.append(num)
                break
        else:

            return -1

    return "".join([str(n) for n in sorted(result)])


print(digitsProduct(450))
