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
