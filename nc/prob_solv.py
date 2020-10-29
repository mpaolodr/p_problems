def csRemoveTheVowels(input_str):

    vowels = {"a", "e", "i", "o", "u", "A", "I", "E", "O", "U"}

    input_copy = input_str

    for i in range(len(input_str) - 1, 0, -1):

        if input_str[i] in vowels:

            input_copy = input_copy[:i] + input_copy[i + 1:]

    return input_copy
