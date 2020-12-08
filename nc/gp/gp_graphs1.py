from collections import deque


class GraphNode:

    def __init__(self, label):

        self.label = label
        self.color = None
        self.neighbors = set()


def color_graph(graph, colors):

    # iterate over each node of the graph
    for node in graph:

        # handle if an infinite loop is occuring
        if node in node.neighbors:
            raise Exception("impossible to find a legal solution")

        # get the node's neighbors colors
        # check if a color is illegal
        illegal_colors = set([
            neighbor.color for neighbor in node.neighbors if neighbor.color
        ])

        # assign the first legal color
        # node.color = colors - illegal_colors # color present in colors but not in illegal colors

        for color in colors:

            if color not in illegal_colors:

                node.color = color
                break

    return graph


graph = {}

a = GraphNode("A")
b = GraphNode("B")
c = GraphNode("C")
d = GraphNode("D")
e = GraphNode("E")
f = GraphNode("F")
g = GraphNode("G")

a.neighbors.add(b)
a.neighbors.add(c)
a.neighbors.add(d)
a.neighbors.add(e)

b.neighbors.add(d)
b.neighbors.add(e)
b.neighbors.add(c)

c.neighbors.add(f)
c.neighbors.add(g)
c.neighbors.add(b)

f.neighbors.add(a)
g.neighbors.add(b)
g.neighbors.add(c)
g.neighbors.add(d)


nodes = [
    a, b, c, d, e, f, g
]

colors = ["black", "white", "red", "yellow", "blue"]

for n in nodes:

    graph[n] = n

color_graph(graph, colors)

for n in nodes:

    print(n.color)


def num_islands(grid):

    # if there is no grid or the grid is empty then
    if grid is None or len(grid) == 0:
        # return zero
        return 0

    # store some lens and an island count

    nr = len(grid)
    nc = len(grid[0])

    island_counts = 0

    #  iterate over each row
    for row in range(nr):

        #  iterate over each col
        for col in range(nc):

            # check if our grid ar[row][col] is 1
            if grid[row][col] == "1":

                # increment the number of islands
                island_counts += 1

                # mark it as visited
                grid[row][col] = "0"

                # set up a queue of neighbors
                neighbors = deque()

                # append row * number_col + col to neighbors
                neighbors.append(row * nc + col)

                # while there are still neighbors
                while len(neighbors) != 0:

                    # set up an id based on a current neighbor
                    id = neighbors.popleft()

                    # set the row
                    row = id // nc
                    # set the column
                    col = id % nc

                    # check all the directions for connected components

                    #  check left
                    if row - 1 >= 0 and grid[row - 1][col] == "1":

                        neighbors.append((row - 1) * nc + col)
                        grid[row - 1][col] = "0"

                    # check right
                    if row + 1 < nr and grid[row + 1][col] == "1":

                        neighbors.append((row + 1) * nc + col)
                        grid[row + 1][col] = "0"

                    # check top
                    if col - 1 >= 0 and grid[row][col - 1] == "1":

                        neighbors.append(row * nc + (col - 1))
                        grid[row][col - 1] = "0"

                    # check bot
                    if col + 1 < nc and grid[row][col + 1] == "1":

                        neighbors.append(row * nc + (col + 1))
                        grid[row][col + 1] = "0"

    return island_counts


"""
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


"""

grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]


grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]


print(num_islands(grid1))
print(num_islands(grid2))
