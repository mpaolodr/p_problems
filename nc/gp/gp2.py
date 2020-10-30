"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
"""


import datetime


def last(a, n):
    # Your code here

    if n > len(a):

        return "Invalid"

    if n == 0:

        return list()

    # return a[len(a) - n:]
    # goes backward starting from end of list
    return a[-n:]


list1 = [1, 2, 3, 4, 5]
list2 = [4, 3, 9, 9, 7, 6]


print(last(list1, 1))
print(last(list2, 3))
print(last(list2, 2))
print(last(list1, 7))
print(last(list1, 0))
print(last(list1, 3))


"""
Challenge #2:

Given a list of numbers, create a function that returns the list but with each
element's index in the list added to itself. You should add 0 to the number at
index 0, add 1 to the number at index 1, etc.

Examples:
- add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
- add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
- add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]

Notes:
- The input list will only contain integers.
"""


def add_indexes(numbers):
    # Your code here

    for i in range(len(numbers)):

        numbers[i] += i

    return numbers


print(add_indexes([0, 0, 0, 0, 0]))
print(add_indexes([1, 2, 3, 4, 5]))
print(add_indexes([5, 4, 3, 2, 1]))


"""
Challenge #3:

Given a string of numbers separated by a comma and space, return the product of the numbers.

Examples:
- multiply_nums("2, 3") ➞ 6
- multiply_nums("1, 2, 3, 4") ➞ 24
- multiply_nums("54, 75, 453, 0") ➞ 0
- multiply_nums("10, -2") ➞ -20

Notes:
- Bonus: Try to complete this challenge in one line!
"""


def multiply_nums(nums):
    # Your code here

    num_list = [int(num) for num in nums.split(", ")]

    product = num_list[0]

    for i in range(1, len(num_list)):

        product *= num_list[i]

    return product


print(multiply_nums("2, 3"))
print(multiply_nums("1, 2, 3, 4"))
print(multiply_nums("54, 75, 453, 0"))
print(multiply_nums("10, -2"))


"""
Challenge #4:

Create a function that changes specific words into emoticons. Given a sentence
as a string, replace the words `smile`, `grin`, `sad`, and `mad` with their
corresponding emoticons.

word -> emoticon
---
smile -> :D
grin -> :)
sad -> :(
mad	-> :P

Examples:
- emotify("Make me smile") ➞ "Make me :D"
- emotify("Make me grin") ➞ "Make me :)"
- emotify("Make me sad") ➞ "Make me :("

Notes:
- The sentence always starts with "Make me".
- Try to solve this without using conditional statements like if/else.
"""


def emotify(txt):
    # Your code here

    emojis = {
        "smile": ":D",
        "grin": ":)",
        "sad": ":(",
        "mad": ":P"
    }

    # emojified = txt.split()

    # for i in range(len(emojified)):

    #     if emojified[i] in emojis:

    #         emojified[i] = emojis[emojified[i]]

    # return " ".join(emojified)

    # OR

    # for key in emojis:

    #     if key in txt:

    #         txt.replace(key, emojis[key])
    #         return txt

    # OR

    new_txt = txt

    for k, v in emojis.items():

        new_txt = new_txt.replace(k, v)

    return new_txt


print(emotify("Make me smile, make me mad, make me sad"))  # ➞ "Make me :D"
print(emotify("Make me grin"))  # ➞ "Make me :)"
print(emotify("Make me sad"))  # ➞ "Make me :("


"""
Challenge #5:

Create a function that returns the data type of a given argument. There are
seven data types this challenge will be testing for:

- List
- Dictionary
- String
- Integer
- Float
- Boolean
- Date

Examples:
- data_type([1, 2, 3, 4]) ➞ "list"
- data_type({'key': "value"}) ➞ "dictionary"
- data_type("This is an example string.") ➞ "string"
- data_type(datetime.date(2018,1,1)) ➞ "date" 

Notes:
- Return the name of the data type as a lowercase string.
"""


def data_type(value):
    # Your code here

    arg_type = str(type(value)).split()[1][:-1]

    data_type = {
        "'datetime.date'": "date",
        "'list'": "list",
        "'dict'": "dictionary",
        "'str'": "string",
        "'float'": "float",
        "'int'": "integer"
    }

    return data_type[arg_type]


print(data_type([1, 2, 3, 4]))  # ➞ "list"
print(data_type({'key': "value"}))  # ➞ "dictionary"
print(data_type("This is an example string."))  # ➞ "string"
print(data_type(datetime.date(2018, 1, 1)))  # ➞ "date"


"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
"""


def get_middle(input_str):
    # Your code here

    pointer1 = 0
    pointer2 = len(input_str) - 1

    while pointer1 < pointer2 - 1:

        pointer1 += 1
        pointer2 -= 1

    return input_str[pointer1: pointer2 + 1]


print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))


"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""


def get_count(input_str):
    # Your code here

    vowels = {"a", "e", "i", "o", "u"}

    count = 0

    for char in input_str:

        if char in vowels:

            count += 1

    return count


print(get_count("aaaaeeeit"))
print(get_count("eat moo"))
print(get_count("task it"))
