
def dijkstra(adjacency_matrix, start_node):
    """ Dijkstra's algorithm for finding the shortest path from a start node 
        to all other nodes in a graph.
        adjacency_matrix:  An adjacency matrix representation of the graph.
        start_node:        The node to start the algorithm from.
        Returns:  A Dictionary with the keys:
            start_node:  The node the paths start from (an integer)
            parent_list:  A list of integers indicating the last node on the
                          path from start to that node.  So for example:
                          [None, 0, 1, 1, 2]  To get from Node 0 (start) to node 4
                          you will arrive via node 2
            shortest_distance:  The distances from the start to the node.
    """
    num_nodes = len(adjacency_matrix)
    
    # Your code here
    
    return {"start_node": start_node, "parent_list": parents,
            "shortest_distances": shortest_distances}
