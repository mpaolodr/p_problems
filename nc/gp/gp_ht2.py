"""
You are given a non-empty list of words.
Write a function that returns the *k* most frequent elements.
The list that you return should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical
order should come first.
Example 1:
```plaintext
Input:
words = ["lambda", "school", "rules", "lambda", "school", "rocks"]
k = 2
Output:
["lambda", "school"]
Explanation:
"lambda" and "school" are the two most frequent words.
```
Example 2:
```plaintext
Input:
words = ["the", "sky", "is", "cloudy", "the", "the", "the", "cloudy", "is", "is"]
k = 4
Output:
["the", "is", "cloudy", "sky"]
Explanation:
"the", "is", "cloudy", and "sky" are the four most frequent words. The words
are sorted from highest frequency to lowest.
```
Notes:
- `k` is always valid: `1 <= k <= number of unique elements.
- words in the input list only contain lowercase letters.
```
"""


import collections


def top_k_frequent(words, k):
    """
    Input:
    words -> List[str]
    k -> int
    Output:
    List[str]
    """

    # Your code here
    # use the python built in dictionary
    dictionary = dict()

    # iterate over each word in the words list
    for word in words:
        # if the word is in our dictionary
        if word in dictionary:
            # then increment the count of that word
            dictionary[word] += 1
        # otherwise
        else:
            # set the count of that word to 1
            dictionary[word] = 1
    # sort the words / keys in our dictionary in descending order
    word_list = sorted(dictionary, key=lambda x: (-dictionary[x], x))

    # return a slice of the sorted words from start of list up to the k - 1 element
    return word_list[:k]


# testing

print(top_k_frequent(["lambda", "school", "rules", "lambda",
                      "school", "rocks"], 2))  # => ["lambda", "school"]
print(top_k_frequent(["the", "sky", "is", "cloudy", "the", "the",
                      "the", "cloudy", "is", "is"], 4))  # => ["the", "is", "cloudy", "sky"]


# demo 2
"""
Given a string, sort it in decreasing order based on the frequency of characters.
Example 1:
```plaintext
Input:
"free"
Output:
"eefr"
Explanation:
'e' appears twice while 'f' and 'r' appear once.
So 'e' must appear before 'f' and 'r'. Therefore, "eerf" is also a valid answer.
```
Example 2:
```plaintext
Input:
"dddbbb"
Output:
"dddbbb"
Explanation:
Both 'd' and 'b' appear three times, so "bbbddd" is also a valid answer.
Note that "dbdbdb" is incorrect, as the same characters must be together.
```
Example 3:
```plaintext
Input:
"Bbcc"
Output:
"ccBb"
Explanation:
"ccbB" is also a valid answer, but "Bbcc" is incorrect.
Note that 'B' and 'b' are treated as two different characters.
```
"""

# use the counter from collections to save us some time


def frequency_sort(s: str) -> str:
    """
    Inputs:
    s -> str
    Output:
    str
    """
    # Your code here
    # count up all of the occurrences of each letter
    # ref: https://docs.python.org/3/library/collections.html#collections.Counter
    letters_count = collections.Counter(s)

    # create a list to build the string
    string_build = list()  # []

    # iterate over the sorted counts (using the ".most_common()" method) extracting the letter and frequency key value pair
    for letter, frequency in letters_count.most_common():
        # letter * frequency
        # "V" * 5 -> "VVVVV"
        # append the letter * frequency to the string_build list
        string_build.append(letter * frequency)

    # turn the list back in to a string and return it (use a join?)
    return "".join(string_build)


print(frequency_sort("free"))  # => "eefr"
print(frequency_sort("dddbbb"))  # => "dddbbb"
