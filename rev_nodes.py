# class Node:
#     def __init__(self, value, next_node=None):

#         self.value = value
#         self.next = next_node


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)
# e = Node(5)
# f = Node(6)
# g = Node(7)
# h = Node(8)

# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# f.next = g
# g.next = h


n1 = ListNode(1)
n1.next = ListNode(2)
n1.next.next = ListNode(3)
n1.next.next.next = ListNode(4)
n1.next.next.next.next = ListNode(5)
n1.next.next.next.next.next = ListNode(6)
n1.next.next.next.next.next.next = ListNode(7)
n1.next.next.next.next.next.next.next = ListNode(8)
n1.next.next.next.next.next.next.next.next = ListNode(9)
n1.next.next.next.next.next.next.next.next.next = ListNode(10)
n1.next.next.next.next.next.next.next.next.next.next = ListNode(11)

# recursive approach

# def rev_in_k(l, k):

#     # keep track of a current node
#     cur = l

#     # 1.  move k nodes across our list to check if our sub-list is long enough
#     # - for this, we iterate with a range of k
#     for _ in range(k):

#         if cur is not None:
#             print(f"THIS IS THE VALUE: {cur.value}")

#         # - we wanna check if we reached the end of the node before the loop ends, then return l
#         if cur is None:

#             return l

#         # - inside this loop, we'll keep moving forward, increment our pointer
#         cur = cur.next

#     # 2. set a reversal ref to l and set current to l.next
#     # rv = l
#     # cur = l.next
#     rv, cur = l, l.next

#     # 3. swap the next k elements by iterating to k - 1
#     for _ in range(k - 1):

#         # **NOTE : Remember to store temp variables before re-assigning
#         # - set current's next pointer to be the reversal reference we declared
#         temp = cur.next
#         cur.next = rv
#         # - set current to current next(increment)
#         temp_cur = cur
#         cur = temp
#         # - set reversal to the current
#         rv = temp_cur

#         # or something like this if you want to avoid storing temporary variables
#         # cur.next, cur, rv = rv, cur.next, cur

#     # 4. recursive call
#     # - connect the head node with the rest of the reversed sub-lists
#     l.next = rev_in_k(cur, k)

#     # 5. return our reversal
#     return rv

# iterative approach - we'll need a helper function
# def reverser(start, end):

#     # set a prev to the end
#     prev = end
#     # set a next_starting_node to the start.next
#     next_starting_node = start.next
#     # set a current_node to start.next
#     current_node = start.next
#     # while the current node is not the end
#     while current_node != end:
#         # swap things
#         # set a temp to the current node's next
#         temp = current_node.next
#         # set current node's next to previous
#         current_node.next = prev
#         # set prev to current node
#         prev = current_node
#         # set current node to temp
#         current_node = temp
#     # set our starting node's next to prev
#     start.next = prev
#     # return our next starting node to the caller
#     return next_starting_node


# def rev_in_k(l, k):

#     # Edge Case # 1
#     # - if l is None
#     # - if l.next is None (we only have one Node)
#     # if k == 1, we don't have to swap anything
#     if l is None or l.next is None or k == 1:
#         # we return l
#         return l

#     # Edge Case # 2
#     # 1. create something to swap with the head of the list because head of the list has no node before it so we create one
#     dummy_list = Node(0)  # -> placeholder to hold the rest of the list
#     # 2. append original list "l" to the end of this list
#     dummy_list.next = l
#     # 3. we set the dummy list as the starting node
#     starting_node = dummy_list
#     # 4.  keep track of some counter
#     counter = 0
#     # 5.  iterate over the whole list
#     while l is not None:

#         # 5a increment our counter
#         counter += 1

#         # 5bif. check if counter % k is 0: keep it inbounds of k
#         if counter % k == 0:  # -> we reached kth node in our list
#             # 5b.1. set starting node to rev of starting node and l.next
#             # 5b.2. call to helper function when we reach kth node
#             starting_node = reverser(starting_node, l.next)
#             # 5b.3. set l(the head) to the starting node's next (moving the head forward)
#             l = starting_node.next

#         # 5belse. move to next node in our list
#         else:
#             # 5belse.1 set l to l.next
#             l = l.next

#     # 6. return the list.next because list is the dummy list we created
#     return dummy_list.next

# Christian's code

# class ListNode(object):
#     def __init__(self, x):
#         self.value = x
#         self.next = None
# Create some sort of reversing helper function:
# def reverse(start, end):
#     # set a prev to the end
#     prev = end
#     # set a next_starting_node to the start.next
#     next_starting_node = start.next
#     # set a current_node to start.next
#     current_node = start.next
#     # while the current node is not the end
#     while current_node != end:
#         # swap things
#         # set a temp to the current node's next
#         temp = current_node.next
#         # set current node's next to previous
#         current_node.next = prev
#         # set prev to current node
#         prev = current_node
#         # set current node to temp
#         current_node = temp
#     # set our starting node's next to prev
#     start.next = prev
#     # return our next starting node to the caller
#     return next_starting_node


# def rev_in_k(l, k):
#     # check base case and edge cases
#     # if l is none
#     # or if l.next is none
#     # or if k == 1
#     if l is None or l.next is None or k == 1:
#         # return l
#         return l
#     # edge case to swap the first item (create a new list)
#     list = ListNode(0)
#     # Append list to the end of this list
#     list.next = l
#     # set list to the head (starting node)
#     starting_node = list
#     # Keep track of some counter.
#     counter = 0
#     # iterate iver hte while list
#     while l:
#         # increment my counter
#         counter += 1
#         # check if counter mod k is zero
#         if counter % k == 0:
#             # starting node to rev of starting node and l.next
#             # call to helper function
#             starting_node = reverse(starting_node, l.next)
#             # else set L (the head) to the string nodes next
#             l = starting_node.next
#         # otherwise
#         else:
#             # traverse forward setting L to L.next
#             l = l.next
#     # return the list.next
#     return list.next


def print_ll(head_node):

    cur = head_node

    while cur is not None:

        if cur.next is not None:

            print(f"{cur.value} -> ", end="")

        else:

            print(f"{cur.value} -> None", end="")

        cur = cur.next


print_ll(n1)
print()
print("-----------")

rev = rev_in_k(n1, 2)
print_ll(rev)  # 2 -> 1 -> 4 -> 3 -> 6 -> 5 -> 8 -> 7 -> None
print()
print("-----------")

# rev = rev_in_k(a, 3)
# print_ll(rev)  # 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 7 -> 8 -> None
# print()
# print("-----------")
