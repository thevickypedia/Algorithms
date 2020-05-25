#! /usr/bin/env python3
# MST


def prims(graph, start_vertex):
    # taking a keys list of (n+1) vertices, so that vertex[i] represent key[i]
    keys = [1000000 for _ in range(len(graph) + 1)]
    mstSet = set()

    # put start vertex in the MST
    mstSet.add(start_vertex)
    keys[start_vertex] = 0

    # update the keys for neighbors of start vertex
    for neighbours in graph[start_vertex]:
        keys[neighbours[0]] = neighbours[1]

    # while all the vertex are not in MST
    while len(mstSet) != len(graph):

        # pick the node with least key
        minDist = 1000000
        min_index = None
        for v in range(1, len(keys)):
            # find the node with minimum key, which is not present in MST
            if keys[v] < minDist and v not in mstSet:
                minDist = keys[v]
                min_index = v

        if min_index is None:
            break

        # add the found vertex in MST
        mstSet.add(min_index)

        # update the keys for neighbors of added node
        for neighbour in graph[min_index]:
            node = neighbour[0]
            cost = neighbour[1]

            # only update keys, if they are less and the node is not already in MST
            if node not in mstSet and keys[node] > cost:
                keys[node] = cost

    # return the sum of keys, ignore position 0, as that is dummy position
    return sum(keys[1:])


def add_edge(G, v1, v2, ce):
    if v1 in G:
        G[v1].append((v2, ce))
    else:
        G[v1] = [(v2, ce)]
    if v2 in G:
        G[v2].append((v1, ce))
    else:
        G[v2] = [(v1, ce)]


if __name__ == '__main__':

    input_filename = input('Please provide an input filename:\n')
    input_vertex = int(input('Please provide a start vertex label (1..n):\n'))

    G = {}
    with open(input_filename, 'r') as input_graph_file:
        n, m = tuple(int(x) for x in input_graph_file.readline().split())
        G = {}
        for line in input_graph_file:
            v1, v2, ce = tuple(int(v) for v in line.split())
            add_edge(G, v1, v2, ce)

    print(prims(G, input_vertex))
