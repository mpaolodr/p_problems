#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def balancedBinaryTree(root):

    if root is None:

        return True

    s = [root]

    while len(s) > 0:

        node = s.pop()

        r_level = 0
        l_level = 0

        if node.right is not None:

            r_level = height(node.right)
            s.append(node.right)

        if node.left is not None:

            l_level = height(node.left)
            s.append(node.left)

        if abs(r_level - l_level) > 1:

            return False

    return True


def height(n):

    levels = list()

    q = [(1, n)]

    while len(q) > 0:

        pair = q.pop(0)

        node = pair[1]
        level = pair[0]

        levels.append((level, node.value))
        if node.left is not None:

            q.append((level + 1, node.left))

        if node.right is not None:

            q.append((level + 1, node.right))

    level_set = set()

    for l in levels:

        level_set.add(l[0])

    return max(level_set)


# def minimumDepthBinaryTree(root):

#     if root is None:

#         return 0

#     paths = list()

#     s = [[root]]

#     while len(s) > 0:

#         p = s.pop()

#         node = p[-1]

#         if node != root:

#             if len(paths) > 0:

#                 replaced = False

#                 for i in range(len(paths)):

#                     nodes_in_p = {n.value for n in p}

#                     if paths[i][-1] in nodes_in_p:

#                         paths[i] = [node.value for node in p]
#                         replaced = True

#                 if not replaced:

#                     paths.append([node.value for node in p])

#             else:

#                 paths.append([node.value for node in p])

#         if node.left is not None:

#             p_copy = list(p) + [node.left]
#             s.append(p_copy)

#         if node.right is not None:

#             p_copy = list(p) + [node.right]
#             s.append(p_copy)

#     return min([len(p) for p in paths]) if len(paths) > 0 else 1


def minimumDepthBinaryTree(root):

    if root is None:

        return 0

    if root.left is None and root.right is None:

        return 1

    if root.left is not None and root.right is None:

        return minimumDepthBinaryTree(root.left) + 1

    if root.right is not None and root.left is None:

        return minimumDepthBinaryTree(root.right) + 1

    return min(minimumDepthBinaryTree(root.left), minimumDepthBinaryTree(root.right)) + 1


def minimumDepthBinaryTree(root):

    s = [[root]]
    paths = list()

    while len(s):

        path = s.pop()
        node = path[-1]

        if node.right is None and node.left is None:

            paths.append(path)

        if node.right is not None:

            new_p = list(path) + [node.right]
            s.append(new_p)

        if node.left is not None:

            new_p = list(path) + [node.left]
            s.append(new_p)

    min_depth = None

    for path in paths:

        if min_depth is None:

            min_depth = len(path)

        if min_depth > len(path):

            min_depth = len(path)

    return min_depth


# test
def balancedBinaryTree(root):
    if root == None:
        return True

    flatList = list()

    def maxDepth(self, counter):
        # nothing return 0
        if self is None:
            flatList.append(counter)
            return

        if self.left is None and self.right is None:
            flatList.append(counter + 1)
            return

        if self.left is None:
            flatList.append(counter + 1)
            return

        if self.right is None:
            flatList.append(counter + 1)
            return

        maxDepth(self.left, counter + 1)
        maxDepth(self.right, counter + 1)

    maxDepth(root, 1)

    minDepth = min(flatList)
    maxDepth = max(flatList)

    if maxDepth > minDepth + 1:
        return False
    else:
        return True


class BST:

    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None


a = BST(5)
a.left = BST(7)
a.right = BST(22)
a.right.left = BST(17)
a.right.right = BST(9)

a1 = BST(5)
b1 = BST(7)
c1 = BST(22)
d1 = BST(17)
e1 = BST(15)
f1 = BST(1)
g1 = BST(9)

a1.right = c1
a1.left = b1

c1.left = d1
c1.right = g1

d1.left = e1

e1.right = f1

print(minimumDepthBinaryTree(a1))
print(minimumDepthBinaryTree(a))
