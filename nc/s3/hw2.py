def traverseTree(t):

    if t is None:

        return []

    nodes = []

    q = [(0, t)]

    while len(q):

        tup = q.pop(0)

        height = tup[0]
        node = tup[1]

        nodes.append(node.value)

        if node.left is not None:

            q.append((height + 1, node.left))

        if node.right is not None:

            q.append((height + 1, node.right))

    return nodes


def binaryTreeInOrderTraversal(root, inorder=None):

    if inorder is None:

        inorder = list()

    if root is not None:

        if root.left is not None:

            binaryTreeInOrderTraversal(root.left, inorder)

        inorder.append(root.value)

        if root.right is not None:

            binaryTreeInOrderTraversal(root.right, inorder)

        return inorder


def treePaths(t):

    if t is None:

        return []

    s = [[t]]
    paths = list()

    while len(s) > 0:

        path = s.pop()
        node = path[-1]

        if node.left is None and node.right is None:

            paths.append(path)

        if node.left is not None:

            new_p = list(path) + [node.left]
            s.append(new_p)

        if node.right is not None:

            new_p = list(path) + [node.right]
            s.append(new_p)

    result = list()

    for p in paths:

        to_str = ""

        for i in range(len(p)):

            if i == len(p) - 1:

                to_str += str(p[i].value)

            else:

                to_str += f"{str(p[i].value)}->"

        result.append(to_str)

    return result[::-1]
