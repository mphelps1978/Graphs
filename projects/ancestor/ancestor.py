from queue import Queue

def earliest_ancestor(ancestors, starting_node):
    graph = {}

    for node in ancestors:
        if node[1] not in graph:
            graph[node[1]] = [node[0]]
        else:
            graph[node[1]].append(node[0])

    if starting_node not in graph:
        return -1

    q = Queue()
    q.put([starting_node])

    found_ancestors = []

    while not q.empty():
        path = q.get()
        vertex = path[-1]

        if vertex not in graph:
            found_ancestors.append(path)
        else:
            for parent in graph[vertex]:
                q.put(path + [parent])

    if len(found_ancestors) == 1:
        return found_ancestors[0][-1]
    else:
        max_length = max([len(path) for path in found_ancestors])
        return min([path[-1] for path in found_ancestors if len(path) == max_length])