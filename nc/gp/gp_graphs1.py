class GraphNode:

    def __init__(self, label):

        self.label = label
        self.color = None
        self.neighbors = set()
