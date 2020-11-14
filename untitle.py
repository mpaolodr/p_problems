# <- 1  2 -> 3 -> None
# | |
# p  c

"""
Given a reference to the head node of a singly-linked list, write a function
that reverses the linked list in place. The function should return the new head
of the reversed list.
In order to do this in O(1) space (in-place), you cannot make a new list, you
need to use the existing nodes.
In order to do this in O(n) time, you should only have to traverse the list
once.
*Note: If you get stuck, try drawing a picture of a small linked list and
running your function by hand. Does it actually work? Also, don't forget to
consider edge cases (like a list with only 1 or 0 elements).*
"""


class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse(head_of_list):
    # Your code here

    cur = head_of_list
    prev = None

    while cur is not None:

        next_node = cur.next

        cur.next = prev

        prev = cur
        cur = next_node

    head_of_list = prev

    return head_of_list


a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)

a.next = b
b.next = c


cur = a

while cur is not None:

    print(cur.value)
    cur = cur.next

x = reverse(a)


cur = x

while cur is not None:

    print(cur.value)
    cur = cur.next
