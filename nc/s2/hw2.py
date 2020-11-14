# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None
#

# TEST


ll = ListNode(1)
ll.next = ListNode(2)
ll.next.next = ListNode(3)
ll.next.next.next = ListNode(4)
ll.next.next.next.next = ListNode(5)


# def reverseNodesInKGroups(l, k):

#     # study. I don't get this
#     # check if length is less than k

#     cur = l

#     for _ in range(k):

#         if cur is None:

#             return l

#         cur = cur.next

#     prev, cur = l, l.next

#     for node in range(k - 1):

#         cur.next, cur, prev = prev, cur.next, cur

#     l.next = reverseNodesInKGroups(cur, k)

#     return prev


# # reverseNodesInKGroups(ll, 3)
# new_ll = reverseNodesInKGroups(ll, 3)

# cur = new_ll

# while cur is not None:

#     print(cur.value)

#     cur = cur.next

# # O(n ^ 2)
# def reverseNodesInKGroups(l, k):

#     if l.next is None or k == 1:

#         return l

#     # if find_target returns None, no need to do anything
#     cur = l
#     prev = None

#     num_eval = get_length(l) // k

#     new_ll = None

#     while num_eval > 0:

#         # find target node which we'll use to stop reversal from current node
#         target_node = find_target(cur, k)

#         if target_node is None:

#             return new_ll

#         # grab target's next_node
#         target_next_node = target_node.next

#         # reverse from current node to target_node
#         head, tail = reverser(cur, target_node)

#         # meaning this is the first evaluation, we set the reversed head to be the new head of modified list
#         if new_ll is None:

#             new_ll = head

#         # meaning this is the first evaluation and previous pointer hasn't moved yet
#         if prev is not None:

#             prev.next = head

#         # after reversal, we set the next node of the target to be the new tail's next node
#         tail.next = target_next_node

#         prev = tail
#         cur = tail.next

#         num_eval -= 1

#     return new_ll


# def find_target(l, k):
#     """
#     Find the node we want to end the reversal
#     """

#     cur = l
#     stopper = 0

#     while cur is not None:

#         if stopper == k - 1:

#             break

#         cur = cur.next
#         stopper += 1

#     return cur


# def reverser(head, target_node):
#     """
#     returns the head and tail of the reversed list
#     """

#     cur = head
#     prev = None

#     while cur is not target_node:

#         prev_next = cur.next

#         cur.next = prev

#         prev = cur
#         cur = prev_next

#     prev_next = cur.next
#     cur.next = prev

#     tail = head
#     head = cur

#     return head, tail


# def get_length(l):
#     """
#     get the length of the linked list
#     """

#     cur = l
#     length = 0

#     while cur is not None:

#         length += 1
#         cur = cur.next

#     return length


def reverseInK(l, k):

    cur = l
    counter = 1

    while cur is not None and counter < k:

        counter += 1
        cur = cur.next

    if cur is None:

        return l

    new_next = cur.next

    head, tail = reverser(l, cur)

    tail.next = reverseInK(new_next, k)

    return head


def reverser(head, target):

    cur = head
    prev = None

    while cur != target:

        next_node = cur.next

        cur.next = prev

        prev = cur
        cur = next_node

    cur.next = prev

    tail = head
    head = cur

    return head, tail

# # Singly-linked lists are already defined with this interface:
# # class ListNode(object):
# #   def __init__(self, x):
# #     self.value = x
# #     self.next = None
# #
# def mergeTwoLinkedLists(l1, l2):

#     if l1 is None and l2 is not None:

#         return l2

#     if l2 is None and l1 is not None:

#         return l1

#     pointer_1 = l1
#     pointer_2 = l2

#     new_ll = None
#     pointer_3 = None

#     while pointer_1 is not None and pointer_2 is not None:

#         if new_ll is None:

#             if pointer_1.value < pointer_2.value:

#                 new_ll = ListNode(pointer_1.value)
#                 pointer_1 = pointer_1.next

#                 pointer_3 = new_ll

#             else:

#                 new_ll = ListNode(pointer_2.value)
#                 pointer_2 = pointer_2.next

#                 pointer_3 = new_ll

#         else:

#             if pointer_1.value < pointer_2.value:

#                 new_node = ListNode(pointer_1.value)

#                 pointer_3.next = new_node
#                 pointer_3 = pointer_3.next

#                 pointer_1 = pointer_1.next

#             else:

#                 new_node = ListNode(pointer_2.value)

#                 pointer_3.next = new_node
#                 pointer_3 = pointer_3.next

#                 pointer_2 = pointer_2.next

#     while pointer_1 is not None:

#         new_node = ListNode(pointer_1.value)

#         pointer_3.next = new_node
#         pointer_3 = pointer_3.next

#         pointer_1 = pointer_1.next

#     while pointer_2 is not None:

#         new_node = ListNode(pointer_2.value)

#         pointer_3.next = new_node
#         pointer_3 = pointer_3.next

#         pointer_2 = pointer_2.next

#     return new_ll


# # Singly-linked lists are already defined with this interface:
# # class ListNode(object):
# #   def __init__(self, x):
# #     self.value = x
# #     self.next = None
# #
# def insertValueIntoSortedLinkedList(l, value):

#     if l is None:

#         new_node = ListNode(value)
#         l = new_node

#         return l

#     if value < l.value:

#         new_node = ListNode(value)
#         new_node.next = l

#         return new_node

#     # traverse the list until end or until we find a node where value is less than the value of that node
#     cur = l
#     prev = None

#     while cur is not None:

#         if value < cur.value:

#             break

#         prev = cur
#         cur = cur.next

#     new_node = ListNode(value)

#     prev.next = new_node
#     new_node.next = cur

#     return l
