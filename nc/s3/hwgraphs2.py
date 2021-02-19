# def csFriendCircles(friendships):

#     # step 1: we create our graph

#     f_graph = dict()

#     for i in range(len(friendships)):

#         for j in range(len(friendships)):

#             if friendships[i][j] == 1:

#                 if i not in f_graph:

#                     f_graph[i] = set()

#                 f_graph[i].add(j)

#     # step 2: BFS for each vertex in our graph keeping track of what's already been visited

#     tracker = set()
#     circles = list()

#     # we sort just in case one of the verices is connected to everything
#     for v in sorted(f_graph, key=lambda x: len(f_graph[x]), reverse=True):

#         if v not in tracker:

#             for s in f_graph[v]:

#                 tracker.add(s)

#             circles.append(list(f_graph[v]))

#     return len(circles)


def DFS(friends, visited, cur_row):

    for col in range(len(friends)):

        if friends[cur_row][col] == 1 and visited[col] == 0:

            if col != cur_row:
                visited[col] = 1
                DFS(friends, visited, col)


def csFriendCircles(friendships):

    circles = 0

    visited = [0] * (len(friendships))

    for i in range(len(friendships)):

        if (visited[i] == 0):

            visited[i] = 1

            DFS(friendships, visited, i)

            circles += 1

    return circles


f1 = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]


f2 = [
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1]
]

f3 = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

f4 = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]

f5 = [
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1]
]


print(csFriendCircles(f1))
print(csFriendCircles(f2))
print(csFriendCircles(f3))
print(csFriendCircles(f4))
print(csFriendCircles(f5))
