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


#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def largestValuesInTreeRows(t):

    if t is None:

        return list()

    result = list()

    level_dict = get_level(t)

    for level in level_dict:

        result.append(max(level_dict[level]))

    return result


def get_level(node):

    q = [[node, 0]]

    level_dict = dict()

    while len(q) > 0:

        level_list = q.pop(0)

        node = level_list[0]
        level = level_list[1]

        if level not in level_dict:

            level_dict[level] = list()

        level_dict[level].append(node.value)

        if node.left is not None:

            q.append([node.left, level + 1])

        if node.right is not None:

            q.append([node.right, level + 1])

    return level_dict
