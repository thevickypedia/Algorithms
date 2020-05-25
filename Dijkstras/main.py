# Adjacency list using Dijkstras
# ! /usr/bin/env python3


def load_adjacency_list(filename):
    lines = open(filename).readlines()
    adj_dict = {}
    for l in lines:
        parts = l.split(' ')
        start = int(parts[0])
        nodes = []
        for p in parts[1:]:
            nodes.append(tuple([int(x) for x in p.split(',')]))
        adj_dict[start] = nodes
    return adj_dict


def findMinDistances(graph, startNode):
    remainingNodes = set(graph.keys())

    visited = [1000000 for _ in range(len(remainingNodes) + 1)]
    visited[startNode] = 0

    while len(remainingNodes) != 0:

        min_node = None

        for node in remainingNodes:
            if min_node is None:
                min_node = node
            elif visited[node] < visited[min_node]:
                min_node = node

        if min_node is None:
            break

        remainingNodes.remove(min_node)

        currentDistance = visited[min_node]

        for (node, distance) in graph[min_node]:

            distance = currentDistance + distance

            if distance < visited[node]:
                visited[node] = distance

    return ','.join([str(x) for x in visited[1:]])


filename = input('Please provide a filename containing an adjacency list: ')
graph = load_adjacency_list(filename)

startNode = int(input('Please provide a start vertex label (1..n): '))
print(findMinDistances(graph, startNode))
