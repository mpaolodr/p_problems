def validBst(root):

    stack = [(root, float('-inf'), float('inf'))]

    while len(stack):

        curr = stack.pop()

        currNode = curr[0]
        currMin = curr[1]
        currMax = curr[2]

        if currNode.val >= currMax or currNode.val <= currMin:

            return False

        if currNode.left != None:

            stack.append((currNode.left, currMin, currNode.val))

        if currNode.right != None:

            stack.append((currNode.right, currNode.val, currMax))

    return True
