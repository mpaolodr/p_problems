class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# a recursive solution


def inorder_traversal_r(root):
    # create an inner helper function
    def helper(root, result):
        # if root exists
        if root:
            # call helper on the left of the root, passing the result list along
            helper(root.left, result)
            # append roots value to the result list
            result.append(root.val)
            # call the helper on the right of the root, passing the result list along
            helper(root.right, result)
    result = []
    helper(root, result)
    return result


def inorder_traversal_i(root):
    # hold the result
    result = []
    # make a stack
    stack = []

    # iterate
    while True:
        # while the root node is not none
        while root:
            # append the root to the stack
            stack.append(root)
            # traverse to the left of the root
            root = root.left

            # if there is no stack
            if not stack:
                # return the result
                return result

            # pop the stack on to a node variable
            node = stack.pop()
            # append the nodes value to the result list
            result.append(node.val)
            # traverse to the tight of the node
            root = node.right


# demo2
"""
You are given the values from a preorder and an inorder tree traversal. Write a
function that can take those inputs and output a binary tree.
*Note: assume that there will not be any duplicates in the tree.*
Example:
Inputs:
preorder = [5,7,22,13,9]
inorder = [7,5,13,22,9]
Output:
    5
   / \
  7  22
    /  \
   13   9
"""

pre_order = [5, 7, 22, 13, 9]

in_order = [7, 5, 13, 22, 9]

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    def helper(in_left=0, in_right=len(inorder)):
        # setup

        # store a pre order index external
        nonlocal preorder_index
        # if there are no elements to construct
        if in_left == in_right:
            # return None
            return None

        # pick the pre order index element as a root
        # set the roots value to the preorder ar pre order index
        root_value = preorder[preorder_index]
        # set a root as a new TreeNode with the root value
        root = TreeNode(root_value)

        # root needs to be split on the in order list
        # needs to be split in to left and right subtrees (maybe a dictionary)
        # and set an index variable
        index = index_map[root_value]

        # now we can do the recursion
        # increment the pre order index
        preorder_index += 1

        # build the left subtree
        # set the roots left to a call of helper passing in "in_left", "index"
        root.left = helper(in_left, index)

        # build the right subtree
        # set the roots right to a call of the helper passing in "index + 1", "in_right"
        root.right = helper(index + 1, in_right)

        # return the root
        return root

    # driver code
    # start from the first pre order element
    # create a pre order index of zero
    preorder_index = 0

    # build a dictionary of value -> its index
    index_map = {}

    # enumerate the index and value of inorder
    for index, value in enumerate(inorder):
        index_map[value] = index

    # return helper()
    return helper()


tree1 = build_tree(pre_order, in_order)


print("Done!")
