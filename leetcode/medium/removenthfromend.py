class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        just like how we move from head by (length - n) times,
         we move a pointer by n + 1 times, and before this pointer
         reaches none, it'll move length - n times since we already moved it by n times

        """

        dummy = ListNode(0, head)

        f = dummy
        s = dummy

        for _ in range(n + 1):

            f = f.next

        while f is not None:

            f = f.next
            s = s.next

        s.next = s.next.next

        return dummy.next

        # first pass
        # if head is None:

        #     return None

        # # we get the length of the list

        # length = 0

        # cur = head

        # while cur is not None:

        #     length += 1
        #     cur = cur.next

        # stop = length - n
        # cur = head
        # prev = None

        # while stop > 0:

        #     prev = cur
        #     cur = cur.next
        #     stop -= 1

        # if prev is None:

        #     if head.next is None:

        #         return None

        #     else:

        #         return head.next

        # else:

        #     if cur.next is None:

        #         prev.next = None
        #         return head

        #     else:

        #         prev.next = cur.next
        #         return head
