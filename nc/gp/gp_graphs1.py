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


g = {}

nodes = [
    GraphNode("A"), GraphNode("B"), GraphNode(
        "C"), GraphNode("D"), GraphNode("E")
]

colors = ["black", "white", "red", "yellow", "blue"]

for n in nodes:

    g[n.label] = n

print(g)
