class Solution:
    def convert(self, s: str, numRows: int) -> str:

        #         if len(s) == 1 or numRows == 1:

        #             return s

        #         # num of columns
        #         numCols = ((len(s) - 1) // numRows) + ((numRows - 2) * (((len(s) - 1) // numRows) - 1))

        #         results = list()

        #         # generate results matrix
        #         for _ in range(numRows):

        #             if numCols <= 0:

        #                 temp = [None] * 1

        #             else:

        #                 temp = [None] * numCols

        #             print(f"{temp} {numCols}")
        #             results.append(temp)

        #         go_diagonal = False
        #         cur_index = 0
        #         i = 0
        #         j = 0

        #         print(results)

        #         while cur_index < len(s):

        #             if i < numRows and not go_diagonal:

        #                 results[i][j] = s[cur_index]

        #                 cur_index += 1
        #                 i += 1

        #             else:

        #                 if i == numRows:

        #                     go_diagonal = True

        #                     i = i - 2
        #                     j += 1

        #                     results[i][j] = s[cur_index]

        #                     i -= 1
        #                     j += 1

        #                     cur_index += 1

        #                 elif i == 0:

        #                     go_diagonal = False

        #                     results[i][j] = s[cur_index]

        #                     i += 1

        #                     cur_index += 1

        #                 else:

        #                     results[i][j] = s[cur_index]

        #                     i -= 1
        #                     j += 1

        #                     cur_index += 1

        #         joined_result = ""

        #         for a in results:

        #             temp = ""

        #             for char in a:

        #                 if char is not None:

        #                     temp += char

        #             joined_result += temp

        #         return joined_result

        if len(s) == 1 or numRows == 1:

            return s

        string_dict = {i: "" for i in range(numRows)}

        counter = 0
        reverse_sequence = False

        for i in range(len(s)):

            string_dict[counter] += s[i]

            if counter == numRows - 1:

                reverse_sequence = True

            else:

                if counter == 0 and reverse_sequence:

                    reverse_sequence = False

            if reverse_sequence:

                counter -= 1

            else:

                counter += 1

        result = ""

        for k in string_dict:

            result += string_dict[k]

        return result
