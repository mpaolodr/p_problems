"""
I have two registers: one for take-out orders, and the other for the other folks eating inside the cafe. All the customer orders get combined into one list for the kitchen, where they should be handled first-come, first-served.

Recently, some customers have been complaining that people who placed orders after them are getting their food first. Yikes—that's not good for business!

To investigate their claims, one afternoon I sat behind the registers with my laptop and recorded:

The take-out orders as they were entered into the system and given to the kitchen. (take_out_orders)
The dine-in orders as they were entered into the system and given to the kitchen. (dine_in_orders)
Each customer order (from either register) as it was finished by the kitchen. (served_orders)
Given all three lists, write a function to check that my service is first-come, first-served. All food should come out in the same order customers requested it.

We'll represent each customer order as a unique integer.

As an example,

  Take Out Orders: [1, 3, 5]
  Dine In Orders: [2, 4, 6]
  Served Orders: [1, 2, 4, 6, 5, 3]
would not be first-come, first-served, since order 3 was requested before order 5 but order 5 was served first.

But,

  Take Out Orders: [17, 8, 24]
  Dine In Orders: [12, 19, 2]
  Served Orders: [17, 8, 12, 19, 24, 2]
would be first-come, first-served.

"""


# first solution
import unittest

# def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):


#     # we check for duplicated orders


#     # we check if all orders are served
#     combined_set = set(take_out_orders).union(set(dine_in_orders))
#     served_set = set(served_orders)

#     if len(combined_set) != len(served_set):

#         return False


#     # check if all orders have been served
#     for order in combined_set:

#         if order not in served_set:

#             return False


#     to = 0
#     di = 0
#     s = 0


#     while to < len(take_out_orders) and di < len(dine_in_orders):

#         if served_orders[s] == take_out_orders[to] or served_orders[s] == dine_in_orders[di]:

#             if served_orders[s] == take_out_orders[to]:

#                 to += 1

#             else:

#                 di += 1

#         else:

#             return False


#         s += 1


#     return True


def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders, to=0, di=0, s=0):

    if len(served_orders) == s:

        if (to < len(take_out_orders)) or (di < len(dine_in_orders)):

            return False

        else:

            return True

    if (to < len(take_out_orders)) and take_out_orders[to] == served_orders[s]:

        to += 1

    elif (di < len(dine_in_orders)) and dine_in_orders[di] == served_orders[s]:

        di += 1

    else:

        return False

    s += 1

    return is_first_come_first_served(take_out_orders, dine_in_orders, served_orders, to, di, s)


# Tests

class Test(unittest.TestCase):

    def test_both_registers_have_same_number_of_orders(self):
        result = is_first_come_first_served(
            [1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_registers_have_different_lengths(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_register_is_empty(self):
        result = is_first_come_first_served([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_served_orders_is_missing_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_served_orders_has_extra_orders(self):
        result = is_first_come_first_served(
            [1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)

    def test_one_register_has_extra_orders(self):
        result = is_first_come_first_served([1, 9], [7, 8], [1, 7, 8])
        self.assertFalse(result)

    def test_one_register_has_unserved_orders(self):
        result = is_first_come_first_served([55, 9], [7, 8], [1, 7, 8, 9])
        self.assertFalse(result)

    def test_order_numbers_are_not_sequential(self):
        result = is_first_come_first_served(
            [27, 12, 18], [55, 31, 8], [55, 31, 8, 27, 12, 18])
        self.assertTrue(result)


unittest.main(verbosity=2)
