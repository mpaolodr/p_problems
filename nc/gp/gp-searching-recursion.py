"""
You are a new author that is working on your first book. You are working on a
series of drafts. Each draft is based on the previous draft. The latest draft
of your book has a serious typo. Since each newer draft is based on the
previous draft, all the drafts after the draft containing the typo also include
the typo.
Suppose you have `n` drafts `[1, 2, 3, ..., n]` and you need to find out the
first one containing the typo (which causes all the following drafts to have
the typo as well).
You are given access to an API tool `containsTypo(draft)` that will return
`True` if the draft contains a typo and `False` if it does not.
You need to implement a function that will find the *first draft that contains
a typo*. Also, you have to pay a fee for every call to `containsTypo()`, so
make sure that your solution minimizes the number of API calls.
Example:
Given `n = 5`, and `draft = 4` is the first draft containing a typo.
containsTypo(3) -> False
containsTypo(5) -> True
containsTypo(4) -> True


are we missing containsTypo?
are we supposed to find the first draft with typo or return a boolean???
"""


def containsTypo(draftNum, typo=4):

    if typo > draftNum:

        return False

    else:

        return True


def firstWithTypo(n, typo):

    drafts = [i for i in range(n + 1)]

    s = 0
    l = len(drafts) - 1

    while s <= l:

        m = (s + l) // 2

        if containsTypo(drafts[m], typo):

            l = m - 1

        elif not containsTypo(drafts[m], typo):

            s = m + 1

    return drafts[s]


a = [1, 2, 3, 4, 5]

# print(containsTypo(3))
# print(containsTypo(5))
# print(containsTypo(4))


print(firstWithTypo(7, 3))
