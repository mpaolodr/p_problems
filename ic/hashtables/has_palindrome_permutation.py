# my solution


# def has_palindrome_permutation(the_string):

#     # Check if any permutation of the input is a palindrome

#     check = set()

#     for char in the_string:

#         if char not in check:

#             check.add(char)

#     if len(check) == len(the_string) - (len(the_string) // 2):

#         return True

#     return False


# different implementation

# def has_palindrome_permutation(the_string):

#     count_dict = dict()

#     for char in the_string:

#         if char not in count_dict:

#             count_dict[char] = 0

#         count_dict[char] += 1

#     odd = 0

#     for k in count_dict:

#         if count_dict[k] % 2 != 0:

#             odd += 1

#     return odd <= 1


# IC solution

def has_palindrome_permutation(the_string):

    seen = set()

    for char in the_string:

        if char not in seen:

            seen.add(char)

        else:

            seen.remove(char)

    return len(seen) <= 1
