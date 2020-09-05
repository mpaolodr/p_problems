"""
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).

The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

If a[i] > b[i], then Alice is awarded 1 point.
If a[i] < b[i], then Bob is awarded 1 point.
If a[i] = b[i], then neither person receives a point.
Comparison points is the total points a person earned.

Given a and b, determine their respective comparison points.

"""


"""
js

function compareTriplets(a, b) {
    //push the results here
    let arr = [];
    let scoreCountA = 0;
    let scoreCountB = 0;

    let lenA = a.length;
    let lenB = b.length;

    for (let i = 0; i < lenA; i++) {
        if(a[i] > b[i] && a[i] !== 0 && b[i] !== 0) {
            scoreCountA += 1;
        } else if (a[i] < b[i] && a[i] !== 0 && b[i] !== 0) {
            scoreCountB+= 1;
        } else if (a[i] === b[i]) {
            scoreCountA += 0;
            scoreCountB += 0;
        } else {
            return;
        }
    }

    arr.push(scoreCountA, scoreCountB);

    return arr;
}

"""

# python


def compareTriplets(a, b):

    scoreA = 0
    scoreB = 0

    for i in range(len(a)):

        if a[i] > b[i] and (a[i] != 0 and b[i] != 0):

            scoreA += 1

        elif a[i] < b[i] and (a[i] != 0 and b[i] != 0):

            socreB += 1

        elif a[i] == b[i]:

            continue

        else:

            return

    return [scoreA, scoreB]
