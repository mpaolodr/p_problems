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
