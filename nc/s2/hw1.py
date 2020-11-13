import string


# def buyAndSellStock(prices):

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


def buyAndSellStock(stock_prices):
    # optimized

    min_price = stock_prices[0]
    max_prof = stock_prices[1] - stock_prices[0]

    for i in range(1, len(stock_prices)):

        cur_price = stock_prices[i]
        possible_profit = cur_price - min_price

        min_price = min(cur_price, min_price)
        max_prof = max(possible_profit, max_prof)

    if max_prof < 0:

        return 0

    else:

        return max_prof


print(buyAndSellStock([6, 3, 1, 2, 5, 4]))  # 4
print(buyAndSellStock([1, 5, 3, 2]))  # 4
print(buyAndSellStock([8, 5, 3, 1]))  # 0
print(buyAndSellStock([3, 100, 1, 97]))  # 97
print(buyAndSellStock([3, 3, 3, 3, 3, 3]))  # 0


def alphabeticShift(inputString):

    to_list = list(inputString)
    lowercase = list(string.ascii_lowercase)

    for i in range(len(to_list)):

        index_of_let = lowercase.index(to_list[i])

        to_list[i] = lowercase[(index_of_let + 1) % len(lowercase)]

    return "".join(to_list)


def validParenthesesSequence(s):

    if len(s) == 0:

        return True

    checker = list()

    for p in s:

        if p == "(":

            checker.append(p)

        else:

            try:

                checker.pop()

            except IndexError:

                return False

    if len(checker) > 0:

        return False

    return True
