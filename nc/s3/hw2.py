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
