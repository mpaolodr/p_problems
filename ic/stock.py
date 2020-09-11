"""
Write an efficient function that takes stock_prices and returns the best profit 
I could have made from one purchase and one sale of one share of Apple stock yesterday.

Example:

stock_prices = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices)
# Returns 6 (buying for $5 and selling for $11)

"""


def get_max_profit(stock_prices):

    # This approach fails because the highest value might come before the lowest one
    # you need to buy first before sell

    # # get max value in list
    # max_value = 0

    # for price in stock_prices:

    #     if price > max_value:

    #         max_value = price

    # # get max difference to represent profit

    # max_profit = 0

    # for price in stock_prices:

    #     if max_value - price > max_profit:

    #         max_profit = max_value - price

    # return max_profit

    # -------------------

    # O(n) runtime O(n) space

    # create dictionary with key as index and value as key
    # stock_dict = dict()

    # for p in range(len(stock_prices)):

    #     stock_dict[p] = stock_prices[p]

    # # grab max_value
    # max_value = (0,)

    # for key in stock_dict:

    #     if stock_dict[key] > max_value[0]:

    #         max_value = (stock_dict[key], key)

    # # get max_profit
    # max_p = 0

    # for key in stock_dict:

    #     # check if it's greater than the current max_profit
    #     if (max_value[0] - stock_dict[key] > max_p) and key < max_value[1]:

    #         max_p = max_value[0] - stock_dict[key]

    # return max_p

    # -------------------

    # # if set up like this, it won't return any losses. it will always return 0 if [10, 9, 8, 7 ,6]

    # min_price = stock_prices[0]
    # max_profit = 0

    # for cur_p in stock_prices:

    #     min_price = min(min_price, cur_p)

    #     profit = cur_p - min_price

    #     max_profit = max(profit, max_profit)

    # return max_profit

    # -------------------

    if len(stock_prices) < 2:

        return "must have at least 2 prices"

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for cur_time in range(1, len(stock_prices)):

        cur_p = stock_prices[cur_time]

        profit = cur_p - min_price

        max_profit = max(max_profit, profit)

        min_price = min(min_price, cur_p)

    return max_profit


stock_prices = [10, 8, 6, 4, 2, 0]  # should return -2
# stock_prices = [10, 7, 5, 8, 11, 9]  # should return 6
# stock_prices = [10, 11, 12, 13, 14, 15]  # should return 5
# stock_prices = [1]

print(get_max_profit(stock_prices))
