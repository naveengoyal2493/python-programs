def find_largest_component(graph):
    visited = []
    largest = 0
    for key in graph.keys():
        total_count = explore(graph, key, visited)
        largest = max(largest, total_count)
    return largest


def explore(graph, current, visited):
    if current in visited:
        return 0
    visited.append(current)
    size = 1
    for neighbour in graph[current]:
        size += explore(graph, neighbour, visited)
    
    return size


graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}


print(find_largest_component(graph))