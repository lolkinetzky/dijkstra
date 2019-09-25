require "pry"

def dijkstra(adjacency_matrix, start_node) 

  #int nVertices = adjacencyMatrix[0].length; 
  num_nodes = adjacency_matrix.length

  # shortest_distances will hold the shortest distances from start_node to i
  # it starts with infinity as the value
  shortest_distances = Array.new(num_nodes, Float::INFINITY)


  # added[i] will be true if the path to i 
  # from the source has been found
  added = Array.new(num_nodes, false)


  # Distance of source vertex from 
  # itself is always 0
  shortest_distances[start_node] = 0
  
  # parent array to store the shortest path tree 
  parents = Array.new(num_nodes)
  # no parent for the start node
  parents[start_node] = nil 


  # Find shortest path for all nodes 
  (num_nodes - 1).times do

    # Pick the minimum distance vertex 
    # from the set of vertices not yet 
    # processed. nearest_node is  
    # always equal to start_node in  
    # first iteration. 
    nearest_node = -1
    shortest_distance = Float::INFINITY
    (0...num_nodes).each do |node_index|
      if (!added[node_index] && 
          shortest_distances[node_index] <  shortest_distance)  
        nearest_node  = node_index
        shortest_distance = shortest_distances[node_index]
      end
    end  

    # Mark the picked vertex as visited
    added[nearest_node] = true; 
    # Update dist value of the 
    # adjacent nodes of the picked node. 
    (0...num_nodes).each do |node_index|
      edge_distance = adjacency_matrix[nearest_node][node_index]; 

      if (edge_distance > 0 && 
          ((shortest_distance + edge_distance) <  
              shortest_distances[node_index]))  
        parents[node_index] = nearest_node; 
        shortest_distances[node_index] = shortest_distance +  
                                        edge_distance 
      end
    end
  end
  return {start_node: start_node, parent_list: parents, shortest_distances: shortest_distances }
end
