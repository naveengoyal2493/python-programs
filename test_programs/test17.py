

class Graph:

    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for first, last in edges:
            if first in self.graph_dict:
                self.graph_dict[first].append(last)
            else:
                self.graph_dict[first] = [last]


    def get_route(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        
        paths = []
        for node in self.graph_dict[start]:
            new_path = self.get_route(node, end, path)
            paths = paths + new_path

        return paths



routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto") 
]

g = Graph(routes)
print(g.get_route("Mumbai", "New York"))