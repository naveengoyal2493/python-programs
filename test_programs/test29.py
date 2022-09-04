
# def depth_first_search(graph, source):
#     stack = [source]
#     while len(stack) > 0:
#         cur = stack.pop()
#         print(cur)
#         for i in graph[cur]:
#             stack.append(i)

# def depth_first_search_recursive(graph, source):
#     print(source)
#     current = source
#     for i in graph[current]:
#         depth_first_search_recursive(graph, i)

# def breadth_first_search(graph, source):
#     print(source)
#     queue = [source]
#     while len(queue) > 0:
#         cur = queue.pop()
#         for i in graph[cur]:
#             print(i)
#             queue.insert(0, i)

def has_path_dfs(graph, src, dest):
    if src == dest:
        return True

    for i in graph[src]:
        if has_path_dfs(graph, i, dest):
            return True

    return False


def has_path_bfs(graph, src, dest):
    queue = [src]
    while len(queue) > 0:
        current = queue.pop()
        if current == dest:
            return True
        
        for i in graph[current]:
            queue.insert(0, i)

    return False


graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

# depth_first_search_recursive(graph, 'a')
# breadth_first_search(graph, 'a')
print(has_path_dfs(graph, 'd', 'c'))
print(has_path_bfs(graph, 'a', 'f'))