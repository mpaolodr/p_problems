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
