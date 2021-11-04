
def dijkstra(adjacency_matrix, start_node):
    """ Dijkstra's algorithm for finding the shortest path from a start node 
        to all other nodes in a graph.
        adjacency_matrix:  An adjacency matrix representation of the graph.
        start_node:        The node to start the algorithm from.
    """
    num_nodes = len(adjacency_matrix)
    #  shortest_distances will hold the shortest distances from start_node to i
    # it starts with infinity as the value
    shortest_distances = [float('inf') for i in range(num_nodes)]

    # added[i] will be true if the path to i
    # from the source has been found
    added = [False for i in range(num_nodes)]
    # added = Array.new(num_nodes, false)

    # Distance of source vertex from
    # itself is always 0
    shortest_distances[start_node] = 0

    # parent array to store the shortest path tree
    parents = [None for i in range(num_nodes)]
    # no parent for the start node
    parents[start_node] = None

    # Find shortest path for all nodes
    for i in range(num_nodes - 1):

        # Pick the minimum distance vertex
        # from the set of vertices not yet
        # processed. nearest_node is
        # always equal to start_node in
        # first iteration.
        nearest_node = -1
        shortest_distance = float('inf')
        # (0...num_nodes).each do |node_index|
        for node_index in range(num_nodes):
            if (not added[node_index] and
                    shortest_distances[node_index] < shortest_distance):

                nearest_node = node_index
                shortest_distance = shortest_distances[node_index]

        # Mark the picked vertex as visited
        added[nearest_node] = True
        # Update dist value of the
        # adjacent nodes of the picked node.
        for node_index in range(len(adjacency_matrix[nearest_node])):
            edge_distance = adjacency_matrix[nearest_node][node_index]

            if (edge_distance > 0 and
                ((shortest_distance + edge_distance) <
                    shortest_distances[node_index])):
                parents[node_index] = nearest_node
                shortest_distances[node_index] = shortest_distance + \
                    edge_distance

    return {"start_node": start_node, "parent_list": parents,
            "shortest_distances": shortest_distances}
