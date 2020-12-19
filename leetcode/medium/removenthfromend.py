class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        # first pass
        if head is None:

            return None

        # we get the length of the list

        length = 0

        cur = head

        while cur is not None:

            length += 1
            cur = cur.next

        stop = length - n
        cur = head
        prev = None

        while stop > 0:

            prev = cur
            cur = cur.next
            stop -= 1

        if prev is None:

            if head.next is None:

                return None

            else:

                return head.next

        else:

            if cur.next is None:

                prev.next = None
                return head

            else:

                prev.next = cur.next
                return head
