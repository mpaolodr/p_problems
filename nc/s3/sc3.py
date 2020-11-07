#
# Binary trees are already defined with this interface:


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


# def csBSTRangeSum(root, lower, upper):
#     total = helper(root, lower, upper, 0)
#     print("my total: ", total)


def csBSTRangeSum(root, lower, upper, total=0):
    # print(total)

    # if lower <= root.value <= upper:

    #     total += root.value

    # if root.left is not None:

    #     total = csBSTRangeSum(root.left, lower, upper, total)

    # if root.right is not None:

    #     total = csBSTRangeSum(root.right, lower, upper, total)

    # return total

    # OR

    left = 0
    right = 0

    if root.left:

        left = csBSTRangeSum(root.left, lower, upper, total)

    if root.right:

        right = csBSTRangeSum(root.right, lower, upper, total)

    if lower <= root.value <= upper:

        total += root.value

    return total + left + right


b = Tree(10)
b.left = Tree(5)
b.right = Tree(15)
b.left.left = Tree(3)
b.left.right = Tree(7)
b.right.right = Tree(18)


a = Tree(10)
a.left = Tree(5)
a.left.left = Tree(3)
a.left.left.left = Tree(1)
a.left.right = Tree(7)
a.left.right.left = Tree(6)
a.right = Tree(15)
a.right.left = Tree(13)
a.right.right = Tree(18)


print(csBSTRangeSum(b, 7, 15))
print(csBSTRangeSum(a, 6, 10))
