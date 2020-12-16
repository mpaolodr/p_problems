# my solution


def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome

    check = set()

    for char in the_string:

        if char not in check:

            check.add(char)

    if len(check) == len(the_string) - (len(the_string) // 2):

        return True

    return False
