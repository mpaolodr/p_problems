def alternatingSort(a):

    if len(a) <= 1:

        return True

    pointer_a = 0
    pointer_b = len(a) - 1

    new_arr = [0] * len(a)

    pointer_c = 0

    while pointer_c < len(new_arr) and pointer_a < pointer_b:

        new_arr[pointer_c] = a[pointer_a]

        pointer_a += 1
        pointer_c += 1

        new_arr[pointer_c] = a[pointer_b]

        pointer_b -= 1
        pointer_c += 1

    if pointer_a == pointer_b:

        new_arr[pointer_c] = a[pointer_b]

    for i in range(len(new_arr) - 1):

        if new_arr[i] >= new_arr[i + 1]:

            return False

    return True


def mutateTheArray(n, a):

    new_arr = [0] * len(a)

    for i in range(len(new_arr)):

        cur_elem = a[i]

        if i == 0:

            first_elem = 0

        else:

            first_elem = a[i - 1]

        if i == len(new_arr) - 1:

            last_elem = 0

        else:

            last_elem = a[i + 1]

        new_arr[i] = first_elem + cur_elem + last_elem

    return new_arr


"""
You are implementing your own programming language and you've decided to add support for merging strings. A typical merge function would take two strings s1 and s2, and return the lexicographically smallest result that can be obtained by placing the symbols of s2 between the symbols of s1 in such a way that maintains the relative order of the characters in each string.

For example, if s1 = "super" and s2 = "tower", the result should be merge(s1, s2) = "stouperwer".

You'd like to make your language more unique, so for your merge function, instead of comparing the characters in the usual lexicographical order, you'll compare them based on how many times they occur in their respective strings (fewer occurrences means the character is considered smaller). If the number of occurrences are equal, then the characters should be compared in the usual lexicographical way. If both number of occurences and characters are equal, you should take the characters from the first string to the result.

Given two strings s1 and s2, return the result of the special merge function you are implementing.

Examples:

s1: "dce"
s2: "cccbd"

Expected Output:
"dcecccbd"


Input:
s1: "super"
s2: "tower"

Expected Output:
"stouperwer"


s1: "kkihj"
s2: "jbsmfoftph"
Output:
"jbsmfoftphk"
Expected Output:
"jbsmfoftphkkihj"


nput:
s1: "uchlmfelno"
s2: "gr"
Output:
"ugcrh"
Expected Output:
"gruchlmfelno"
"""

# OPTIMIZE


def concatenationsSum(a):

    concatenated = list()

    for i in range(len(a)):

        for j in range(len(a)):

            concatenated.append(int(f"{a[i]}{a[j]}"))

    return sum(concatenated)
