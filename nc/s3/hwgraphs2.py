def csFriendCircles(friendships):

    # step 1: we create our graph

    f_graph = dict()

    for i in range(len(friendships)):

        for j in range(len(friendships)):

            if friendships[i][j] == 1:

                if i not in f_graph:

                    f_graph[i] = set()

                f_graph[i].add(j)

    # step 2: BFS for each vertex in our graph keeping track of what's already been visited

    tracker = set()
    circles = list()

    # we sort just in case one of the verices is connected to everything
    for v in sorted(f_graph, key=lambda x: len(f_graph[x]), reverse=True):

        if v not in tracker:

            for s in f_graph[v]:

                tracker.add(s)

            circles.append(list(f_graph[v]))

    return len(circles)
