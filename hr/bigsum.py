"""
In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

Function Description

Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.

aVeryBigSum has the following parameter(s):

int ar[n]: an array of integers .
Return

long: the sum of all array elements

"""


"""
js

function aVeryBigSum(ar) {
    return ar.reduce((acc, cv) => {
        return acc + cv;
    }, 0)

}

"""

# python


def aVeryBigSum(ar):

    return sum(ar)
