class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def queueOnStacks(requests):
    left = Stack()
    right = Stack()

    def insert(x):
        left.push(x)

    def remove():

        while not left.isEmpty():

            value = left.pop()
            right.push(value)

        removed_item = right.pop()

        while not right.isEmpty():

            value = right.pop()
            left.push(value)

        return removed_item

    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans


def validBracketSequence(sequence):

    if sequence == "":

        return True

    pair = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    s = []

    for char in sequence:

        # since by default, we're checking the keys of a dictionary
        if char in pair:

            s.append(char)

        else:

            try:

                opening = s.pop()

            except IndexError:

                return False

            if char != pair[opening]:

                return False

    if len(s) > 0:

        return False

    return True
