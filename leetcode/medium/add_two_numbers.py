class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        current1 = l1
        current2 = l2
        # (2,5)

        str1 = self.to_string(l1)
        str2 = self.to_string(l2)

        # 807
        value = int(str1[::-1]) + int(str2[::-1])

        # [7, 0, 8]
        new = [int(x) for x in str(value)][::-1]

        new_head = self.new_ll(new)

        return new_head

    # concatenate all values of linked list
    def to_string(self, head):

        converted = ""

        cur = head

        while cur is not None:

            converted += str(cur.val)
            cur = cur.next

        return converted  # concatenated values of linked list

    # given an array, create a new linked list from each of its values
    def new_ll(self, arr):

        new_head = None

        for i in reversed(range(len(arr))):

            new_node = ListNode(arr[i])

            if new_head is None:

                new_head = new_node

            else:

                prev_head = new_head
                new_head = new_node
                new_head.next = prev_head

        return new_head
