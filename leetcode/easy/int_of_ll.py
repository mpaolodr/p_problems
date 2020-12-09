# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def getListLen(head):
    count = 0

    p = head

    while p is not None:
        count += 1
        p = p.next

    return count


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        # O(n) time complexity
        # O(n) space complexity

#         seen = set()

#         p = headA

#         while p is not None:
#             seen.add(p)

#             p = p.next


#         p = headB

#         while p is not None:
#             if p in seen:
#                 return p

#             p = p.next


#         return None

        # keep current pointers per list
        pa = headA
        pb = headB

        # grab lengths and compute difference
        len_a = getListLen(headA)
        len_b = getListLen(headB)

        # if positive, a is longer, skip in list a
        # if negative, b is longer, skip in list b
        len_diff = len_a - len_b

        if len_diff != 0:

            nodes_to_skip = abs(len_diff)

            for _ in range(nodes_to_skip):

                # list a is longer
                if len_diff > 0:
                    pa = pa.next
                # list b is longer
                else:
                    pb = pb.next

        # Move pointers lockstep, see when they become the same
        while pa is not None:

            if pa is pb:
                return pa

            pa = pa.next
            pb = pb.next

        return None
