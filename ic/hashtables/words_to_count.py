import unittest


class WordCloudData(object):

    def __init__(self, input_string):

        # Count the frequency of each word

        self.words_to_counts = {}
        self.split_words(input_string)

    def split_words(self, input_string):

        cur_start_index = 0
        cur_word_length = 0

        for i, char in enumerate(input_string):

            if len(input_string) - 1 == i:

                if char.isalpha():

                    cur_word_length += 1

                if cur_word_length > 0:

                    word = input_string[cur_start_index:
                                        cur_start_index + cur_word_length]

                    self.add_to_dict(word)

            elif char == " " or char == "\u2014":

                if cur_word_length > 0:

                    word = input_string[cur_start_index:
                                        cur_start_index + cur_word_length]

                    self.add_to_dict(word)

                    cur_word_length = 0

            elif char == ".":

                if i < len(input_string) - 1 and input_string[i + 1] == ".":

                    if cur_word_length > 0:

                        word = input_string[cur_start_index:
                                            cur_start_index + cur_word_length]

                        self.add_to_dict(word)

                        cur_word_length = 0

            elif char.isalpha() or char == "\'":

                if cur_word_length == 0:

                    cur_start_index = i

                cur_word_length += 1

            elif char == "-":

                if i > 0 and input_string[i - 1].isalpha() and input_string[i + 1].isalpha():

                    cur_word_length += 1

                else:

                    if cur_word_length > 0:

                        word = input_string[cur_start_index:
                                            cur_start_index + cur_word_length]

                        self.add_to_dict(word)

                        cur_word_length = 0

    def add_to_dict(self, word):

        if word in self.words_to_counts:

            self.words_to_counts[word] += 1

        elif word.lower() in self.words_to_counts:

            self.words_to_counts[word.lower()] += 1

        elif word.capitalize() in self.words_to_counts:

            self.words_to_counts[word] = 1
            self.words_to_counts[word] += self.words_to_counts[word.capitalize()]

            del self.words_to_counts[word.capitalize()]

        else:

            self.words_to_counts[word] = 1
