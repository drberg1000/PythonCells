class Vertex(object):
    def __init__(self):
        self.neighbors = set()

    def add_neighbor(self, neighbor):
        self.neighbors.add(neighbor)


class Graph(object):
    def __init__(self):
        self.vertices = None

    def from_adjacency_list(self, list_stream):
        # FIXME Don't use readlines()  The entire file shouldn't be read at once.
        split = list_stream.readlines()
        clean = [x.strip() for x in split if len(x.strip()) > 0]
        self.vertices = clean
        # FIXME Needs additional processing after writing additional tests.

    def __len__(self):
        return len(self.vertices)
