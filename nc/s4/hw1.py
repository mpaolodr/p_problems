def csFindTheSingleNumber(nums):

    # first solution
    count_dict = dict()

    for n in nums:

        if n not in count_dict:

            count_dict[n] = 0

        count_dict[n] += 1

    for k in count_dict:

        if count_dict[k] == 1:

            return k


def csAverageOfTopFive(scores):

    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    score_dict = dict()

    for s in sorted_scores:

        if s[0] not in score_dict:

            score_dict[s[0]] = list()

        score_dict[s[0]].append(s[1])

    average_dict = dict()

    for k in score_dict:

        average = sum(score_dict[k][0:5])

        if len(score_dict[k]) >= 5:

            average_dict[k] = [k, average // 5]

        else:

            average_dict[k] = [k, average // len(score_dict[k])]

    sorted_average = [average_dict[key] for key in sorted(average_dict)]

    return sorted_average


# no hash table
# def csAverageOfTopFive(scores):

#     num_students = len(set([pair[0] for pair in scores]))
#     result = list()

#     i = 1

#     while i < num_students + 1:

#         final_list = []
#         scores_arr = []
#         average_score = []

#         for j in range(len(scores)):

#             student = scores[j][0]
#             score = scores[j][1]

#             if student == i:
#                 scores_arr.append(score)

#         scores_arr.sort(reverse=True)

#         if len(scores_arr) >= 5:

#             sum_it = sum(scores_arr[0:5]) // 5

#         else:

#             sum_it = sum(scores_arr) // len(scores_arr)

#         average_score.append(sum_it)

#         final_list = [i] + average_score

#         result.append(final_list)

#         i += 1

#     return result


def csMaxNumberOfLambdas(text):

    lambda_dict = {
        "l": 1,
        "a": 2,
        "m": 1,
        "b": 1,
        "d": 1
    }

    char_count = dict()

    for c in text:

        if c not in char_count:

            char_count[c] = 0

        char_count[c] += 1

    word_count = 0

    valid = True

    while valid:

        for k in lambda_dict:

            if k not in char_count:

                return 0

            if char_count[k] != 0 and lambda_dict[k] <= char_count[k]:

                char_count[k] -= lambda_dict[k]

            else:

                valid = False
                return word_count

        word_count += 1
