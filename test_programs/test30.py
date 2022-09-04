
def has_path(graph, src, dest, visited):
    
    if src == dest:
        return True

    if src in visited:
        return False
    
    visited.append(src)
    
    for neighbour in graph[src]:
        if has_path(graph, neighbour, dest, visited):
            return True

    return False

def adjacency_list(edges):
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

edges = [['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']]

print(has_path(adjacency_list(edges), 'n', 'k', []))