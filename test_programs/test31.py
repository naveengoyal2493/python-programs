

def count_components(graph):
    visited = []
    count = 0
    for key in graph.keys():
        if explore(graph, key, visited) == True:
            count += 1
    return count


def explore(graph, current, visited):
    if current in visited:
        return False
    visited.append(current)
    for neighbour in graph[current]:
        explore(graph, neighbour, visited)

    return True


graph = {
    3: [],
    4: [6],
    6: [4,5,7,8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1]
}

print(count_components(graph))



