"""
Given an array of integers, find the sum of its elements.

Example:
ar = [1 2 3 4 10 11]

-> 31


"""

# python


def simpleArraySum(ar):

    return sum(ar)


"""
 js

function simpleArraySum(ar) {
    /*
     * Write your code here.
     */

    return ar.reduce((acc, cv) => {
        return acc + cv;
    },0)

}
"""
