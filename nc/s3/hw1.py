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


def minimumDepthBinaryTree(root):

    if root is None:

        return 0

    paths = list()

    s = [[root]]

    while len(s) > 0:

        p = s.pop()

        node = p[-1]

        if node != root:

            if len(paths) > 0:

                replaced = False

                for i in range(len(paths)):

                    nodes_in_p = {n.value for n in p}

                    if paths[i][-1] in nodes_in_p:

                        paths[i] = [node.value for node in p]
                        replaced = True

                if not replaced:

                    paths.append([node.value for node in p])

            else:

                paths.append([node.value for node in p])

        if node.left is not None:

            p_copy = list(p) + [node.left]
            s.append(p_copy)

        if node.right is not None:

            p_copy = list(p) + [node.right]
            s.append(p_copy)

    return min([len(p) for p in paths]) if len(paths) > 0 else 1
