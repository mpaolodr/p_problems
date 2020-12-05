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

# everything below should work
# def balancedBinaryTree(root):
#     if root is None:
#         return True

#     flatList = list()

#     def maxDepth(self, counter):


#         # nothing return 0
#         if self is None:
#             flatList.append(counter)
#             return

#         if self.left is None and self.right is None:
#             flatList.append(counter)
#             return

#         if self.left is None and self.right is not None:
#             flatList.append(counter + 1)
#             return

#         if self.right is None and self.left is not None:
#             flatList.append(counter + 1)
#             return

#         maxDepth(self.left, counter + 1)
#         maxDepth(self.right, counter + 1)


#     s = [root]


#     while len(s):

#         flatList = list()
#         node = s.pop()

#         l_height = 0
#         r_height = 0

#         if node.left is not None:

#             maxDepth(node.left, 1)
#             l_height = max(flatList)

#             s.append(node.left)

#         flatList = list()

#         if node.right is not None:
#             maxDepth(node.right, 1)
#             r_height = max(flatList)

#             s.append(node.right)


#         if max(r_height, l_height) - min(r_height, l_height) > 1:

#             return False


#     return True


# def balancedBinaryTree(root):

#     if root == None:
#         return True

#     def maxDepth(self, counter):
#         # node is None so we return 0
#         if self is None:
#             return (0, )
#         # left and right is None, we return counter which starts at 1
#         if self.left is None and self.right is  None:
#             return (counter,)
#         # if one of the legs is dead loop the other back in
#         # added self.right is not None
#         if self.left is None:

#             return(maxDepth(self.right, counter + 1),)

#         # added self.left is not None
#         if self.right is None:

#             return(maxDepth(self.left, counter + 1),)

#         # if neither leg is dead loop both back in
#         return(maxDepth(self.left, counter + 1), maxDepth(self.right, counter + 1))

#     # nothing changed here
#     def flatten2list(object):
#         gather = []
#         for item in object:
#             if isinstance(item, (list, tuple, set)):
#                 gather.extend(flatten2list(item))
#             else:
#                 gather.append(item)
#         return gather


#     # traverse the tree and check the left and right height of each node
#     s = [root]

#     while len(s):

#         node = s.pop()

#         l = 0
#         r = 0

#         if node.left is not None:

#             l = max(flatten2list(maxDepth(node.left, 1)))
#             s.append(node.left)

#         if node.right is not None:

#             r = max(flatten2list(maxDepth(node.right, 1)))
#             s.append(node.right)


#         if max(l, r) - min(l, r) > 1:

#             return False


#     return True


def balancedBinaryTree(root):

    fail_counter = 0

    if root == None:
        return True

    elif root.left is None and root.right is None:
        return True

    def maxDepth(self):
        # nothing return 0
        if self is None:
            return 0

        if self.left is None and self.right is None:
            return 1

        if self.left is None:

            return maxDepth(self.right) + 1

        if self.right is None:

            return maxDepth(self.left) + 1

        return max(maxDepth(self.left), maxDepth(self.right)) + 1

    def inorder_traversal(root):

        if not root:
            return 0

        left = inorder_traversal(root.left)
        right = inorder_traversal(root.right)

        if root.left:

            left_num = maxDepth(root.left)

        else:

            left_num = 0

        if root.right:

            right_num = maxDepth(root.right)

        else:
            right_num = 0

        if max(right_num, left_num) - min(right_num, left_num) > 1:

            nonlocal fail_counter
            fail_counter += 1

    inorder_traversal(root)

    # print (fail_counter, "FAILS")
    if fail_counter > 0:
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
