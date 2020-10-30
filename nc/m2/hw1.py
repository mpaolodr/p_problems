import string


def buyAndSellStock(prices):

    if len(prices) == 1:

        return 0

    # max_profit = prices[1] - prices[0] if prices[1] - prices[0] >= 0 else 0

    # for i in range(len(prices) - 1):

    #     for j in range(i + 1, len(prices)):

    #         if prices[j] - prices[i] > max_profit:

    #             max_profit = prices[j] - prices[i]

    # return max_profit

    min_price = prices[0]
    max_profit = prices[1] - prices[0]

    for time in range(1, len(prices)):

        cur_price = prices[time]

        possible_profit = cur_price - min_price
        max_profit = max(possible_profit, max_profit)

        min_price = min(min_price, cur_price)

    return max_profit if max_profit > 0 else 0


def alphabeticShift(inputString):

    to_list = list(inputString)
    lowercase = list(string.ascii_lowercase)

    for i in range(len(to_list)):

        index_of_let = lowercase.index(to_list[i])

        to_list[i] = lowercase[(index_of_let + 1) % len(lowercase)]

    return "".join(to_list)
