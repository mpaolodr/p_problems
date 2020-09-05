"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
"""

"""
js

function diagonalDifference(arr) {
    // Write your code here

    let firstDiag = arr.map((row, i) => {
        return row[i]
    })
    let secondDiag = arr.reverse().map((row, i) => {
        return row[i];
    })


    //total each diag
    const sumOne = firstDiag.reduce((acc, cv) => {
        return acc + cv;
    })
    const sumTwo = secondDiag.reduce((acc, cv) => {
        return acc + cv;
    })

    return Math.abs(sumOne - sumTwo);
    
}

"""


def diagonalDifference(arr):

    first_d = [row[i] for i, row in enumerate(arr)]
    second_d = [row[i] for i, row in enumerate(arr[::-1])]

    sum_one = sum(first_d)
    sum_two = sum(second_d)

    return abs(sum_one - sum_two)
