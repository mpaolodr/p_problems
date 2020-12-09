# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        cur = head

        while cur is not None:
            if hasattr(cur, "visited"):
                return True

            cur.visited = True
            cur = cur.next

        return False


#         if head:

#             q = []
#             visited = set()
#             connected = False


#             q.append(head)

#             while len(q) > 0:
#                 node = q.pop(0)

#                 if node not in visited:
#                     visited.add(node)

#                     if node.next is not None:
#                         q.append(node.next)

#                 else:
#                     connected = True


#             return connected

#         else:

#             return False
