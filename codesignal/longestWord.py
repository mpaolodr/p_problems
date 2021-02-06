def longestWord(text):

    new_list = list(text)

    for i in range(len(new_list)):

        if not new_list[i].isalpha():

            new_list[i] = " "

    words = "".join(new_list).split()

    longest = ""

    for i in range(len(words)):

        modified = ""

        for char in words[i]:

            if char.isalpha():

                modified += char

        words[i] = modified

    for word in words:

        if len(word) > len(longest):

            longest = word

    return longest
