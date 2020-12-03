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
