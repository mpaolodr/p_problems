#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def traverseTree(t):

    if t is None:

        return list()

    q = [t]
    result = list()

    while len(q) > 0:

        node = q.pop(0)

        result.append(node.value)

        if node.left is not None:

            q.append(node.left)

        if node.right is not None:

            q.append(node.right)

    return result
