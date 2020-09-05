"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with 6 places after the decimal.

"""

"""
function plusMinus(arr) {
    const negArr = [];
    const posArr = [];
    const zero = [];
    const result = [];

    arr.forEach(num => {
        if (num < 0 ) {
            negArr.push(num);
        } else if (num > 0) {
            posArr.push(num)
        } else {
            zero.push(num)
        }
    })

    result.push(negArr.length / arr.length);
    result.push(posArr.length / arr.length);
    result.push(zero.length / arr.length);

   console.log(result[1]);
   console.log(result[0]);
   console.log(result[2]);
}

"""

# python


def plusMinus(arr):

    negArr = []
    posArr = []
    zero = []
    res = []

    for num in arr:

        if num < 0:
            negArr.append(num)

        elif num > 0:
            posArr.append(num)

        else:
            zero.push(num)

    res.append(len(negArr) / len(arr))
    res.append(len(posArr) / len(arr))
    res.append(len(zero) / len(arr))

    print(f"{res[1]:6f}")
    print(f"{res[0]:6f}")
    print(f"{res[2]:6f}")
