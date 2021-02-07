def solution(S, K):
    # write your code in Python 3.6

    days = {
        0: "Mon",
        1: "Tue",
        2: "Wed",
        3: "Thu",
        4: "Fri",
        5: "Sat",
        6: "Sun"
    }

    given_day = 0

    for k in days:

        if days[k] == S:

            given_day = k

    return days[(given_day + K) % len(days)]


print(solution("Wed", 2))
print(solution("Sat", 23))
