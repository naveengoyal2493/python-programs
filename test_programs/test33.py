
from turtle import distance


def build_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if not a in graph:
            graph[a] = []
        if not b in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    
    return graph

def find_shortest_path(graph, src, dest):
    visited = []
    queue = [[src, 0]]
    while len(queue) > 0:
        node, distance = queue.pop()

        if node == dest:
            return distance

        for neighbour in graph[node]:
            queue.insert(0, [neighbour, distance + 1])
    return queue


edges = [['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']]

print(build_graph(edges))

print(find_shortest_path(build_graph(edges), 'w', 'y'))

