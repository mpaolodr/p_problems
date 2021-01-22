def buildPalindrome(st):

    last_elem = st[-1]

    i = 0

    result = ""

    while i < len(st):

        if st + result[::-1] == (st + result[::-1])[::-1]:

            return (st + result[::-1])[::-1]

        result += st[i]

        i += 1
