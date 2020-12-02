# demo 2
"""
You are given a binary tree. You need to write a function that can determin if
it is a valid binary search tree.
The rules for a valid binary search tree are:
- The node's left subtree only contains nodes with values less than the node's
value.
- The node's right subtree only contains nodes with values greater than the
node's value.
- Both the left and right subtrees must also be valid binary search trees.
Example 1:
Input:
    5
   / \
  3   7
Output: True
Example 2:
Input:
    10
   / \
  2   8
     / \
    6  12
Output: False
Explanation: The root node's value is 10 but its right child's value is 8.
"""
# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def is_valid_BST(self, root):

        s, inorder = [], float(-math.inf)

        while s or root:

            while root:

                s.append(root)
                root = root.left

            root = s.pop()

            if root.value <= inorder:

                return False

            inorder = root.value

            root = root.right

        return True

    # def is_valid_BST(self, root):
    #     # Your code here

    #     s = [root]

    #     while len(s) > 0:

    #         node = s.pop()

    #         if node.right is not None:

    #             if min(self.check_max(node.right)) < node.value:

    #                 return False

    #             else:

    #                 s.append(node.right)

    #         if node.left is not None:

    #             if max(self.check_max(node.left)) > node.value:

    #                 return False

    #             else:

    #                 s.append(node.left)

    #     return True

    # def check_max(self, root):

    #     s = [root]
    #     values = list()

    #     while len(s) > 0:

    #         node = s.pop()

    #         values.append(node.value)

    #         if node.left is not None:

    #             s.append(node.left)

    #         if node.right is not None:

    #             s.append(node.right)

    #     return values


b1 = TreeNode(5)
b1.left = TreeNode(3)
b1.right = TreeNode(7)


b2 = TreeNode(10)
b2.left = TreeNode(2)
b2.right = TreeNode(8)
b2.right.left = TreeNode(6)
b2.right.right = TreeNode(12)

b3 = TreeNode(10)
b3.right = TreeNode(13)
b3.right.left = TreeNode(11)
b3.right.right = TreeNode(15)

print(b1.is_valid_BST(b1))
print(b2.is_valid_BST(b2))
print(b3.is_valid_BST(b3))


# demo 1
"""
You are given a binary tree.
Write a function that can find the **maximum depth** of the binary tree. The
maximum depth can be defined as the number of nodes found along the longest
path from the root down to the furthest leaf node. Remember, a leaf node is a
node that has no children.
Example:
Given the following binary tree
    5
   / \
  12  32
     /  \
    8    4
your function should return the depth = 3.
"""


class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):

        if value < self.value:

            if self.left is None:

                self.left = BinaryTreeNode(value)

            else:

                self.left.insert(value)

        else:

            if self.right is None:

                self.right = BinaryTreeNode(value)

            else:

                self.right.insert(value)

    def maxDepth(self, root):
        # Your code here

        # base case of empty tree
        # if root is None:

        #     return 0

        # # get left height
        # left_height = self.maxDepth(root.left)

        # # get right height
        # right_height = self.maxDepth(root.right)

        # return max(left_height, right_height) + 1

        # my solution
        # left_height = 0
        # right_height = 0
        # # get left height
        # if root.left is not None:
        #     left_height = self.maxDepth(root.left)

        # # get right height
        # if root.right is not None:
        #     right_height = self.maxDepth(root.right)

        # return max(left_height, right_height) + 1

        s = []

        if root is not None:

            s.append((1, root))

        depth = 0

        while len(s) > 0:

            cur_depth, root = s.pop()

            if root is not None:

                depth = max(depth, cur_depth)

                s.append((cur_depth + 1, root.left))
                s.append((cur_depth + 1, root.right))

        return depth


b1 = BinaryTreeNode(20)
b1.insert(10)
b1.insert(30)
b1.insert(31)
b1.insert(32)

print(b1.maxDepth(b1))
