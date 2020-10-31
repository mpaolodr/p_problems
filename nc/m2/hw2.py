# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#


def reverseNodesInKGroups(l, k):

    if l.next is None or k == 1:

        return l

    # if find_target returns None, no need to do anything
    cur = l
    prev = None

    num_eval = get_length(l) // k

    new_ll = None

    while num_eval > 0:

        # find target node which we'll use to stop reversal from current node
        target_node = find_target(cur, k)

        if target_node is None:

            return new_ll

        # grab target's next_node
        target_next_node = target_node.next

        # reverse from current node to target_node
        head, tail = reverser(cur, target_node)

        # meaning this is the first evaluation, we set the reversed head to be the new head of modified list
        if new_ll is None:

            new_ll = head

        # meaning this is the first evaluation and previous pointer hasn't moved yet
        if prev is not None:

            prev.next = head

        # after reversal, we set the next node of the target to be the new tail's next node
        tail.next = target_next_node

        prev = tail
        cur = tail.next

        num_eval -= 1

    return new_ll


def find_target(l, k):
    """
    Find the node we want to end the reversal
    """

    cur = l
    stopper = 0

    while cur is not None:

        if stopper == k - 1:

            break

        cur = cur.next
        stopper += 1

    return cur


def reverser(head, target_node):
    """
    returns the head and tail of the reversed list
    """

    cur = head
    prev = None

    while cur is not target_node:

        prev_next = cur.next

        cur.next = prev

        prev = cur
        cur = prev_next

    prev_next = cur.next
    cur.next = prev

    tail = head
    head = cur

    return head, tail


def get_length(l):
    """
    get the length of the linked list
    """

    cur = l
    length = 0

    while cur is not None:

        length += 1
        cur = cur.next

    return length
