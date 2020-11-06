def csFindAllPathsFromAToB(graph):

    s = [[0]]
    paths = list()

    while len(s) > 0:

        p = s.pop()

        v = p[-1]

        if v == len(graph) - 1:

            paths.append(p)

        for nbr in graph[v][::-1]:

            new_p = list(p) + [nbr]
            print(new_p)
            s.append(new_p)

    return paths
