import pytest
from lib.dijkstra import dijkstra

def test_with_sample_matrix():
    # Arrange
    adjacency_matrix =[ 
      [ 0, 4, 0, 0, 0, 0, 0, 8, 0 ], 
      [ 4, 0, 8, 0, 0, 0, 0, 11, 0 ], 
      [ 0, 8, 0, 7, 0, 4, 0, 0, 2 ], 
      [ 0, 0, 7, 0, 9, 14, 0, 0, 0 ], 
      [ 0, 0, 0, 9, 0, 10, 0, 0, 0 ], 
      [ 0, 0, 4, 14, 10, 0, 2, 0, 0 ], 
      [ 0, 0, 0, 0, 0, 2, 0, 1, 6 ], 
      [ 8, 11, 0, 0, 0, 0, 1, 0, 7 ], 
      [ 0, 0, 2, 0, 0, 0, 6, 7, 0 ] 
    ]

    # Act
    answer = dijkstra(adjacency_matrix, 0)

    assert answer == {
        "start_node": 0, 
        "parent_list": [None, 0, 1, 2, 5, 6, 7, 0, 2], 
        "shortest_distances": [0, 4, 12, 19, 21, 11, 9, 8, 14]
    }


def test_dijkstra_with_small_graph():
    # Arrange
    adjacency_matrix =[ 
      [0, 4, 0, 0],
      [4, 0, 12, 6],
      [0, 12, 0, 0],
      [0,  6, 0, 0]
    ]

    # Act
    answer = dijkstra(adjacency_matrix, 0)

    assert answer == {
        "start_node": 0, 
        "parent_list": [None, 0, 1, 1], 
        "shortest_distances": [0, 4, 16, 10]
    }


def test_dijkstra_with_unconnected_graph():
    # Arrange
    adjacency_matrix =[ 
      [0, 4, 0, 0],
      [4, 0, 12, 0],
      [0, 12, 0, 0],
      [0,  0, 0, 0]
    ]

    # Act
    answer = dijkstra(adjacency_matrix, 0)

    assert answer == {
        "start_node": 0, 
        "parent_list": [None, 0, 1, None],
        "shortest_distances": [0, 4, 16, float('inf')]
    }

def test_dijkstra_with_starting_node_other_than_0():
    # Arrange
    adjacency_matrix =[ 
      [0, 4, 0, 0],
      [4, 0, 12, 0],
      [0, 12, 0, 0],
      [0,  0, 0, 0]
    ]

    # Act
    answer = dijkstra(adjacency_matrix, 2)

    assert answer == {
        "start_node": 2, 
        "parent_list": [1, 2, None, None], 
        "shortest_distances": [16, 12, 0, float('inf')]
    }

def test_dijkstra_will_report_no_connections_for_starting_at_unconnected_node():
    # Arrange
    adjacency_matrix =[ 
      [0, 4, 0, 0],
      [4, 0, 12, 0],
      [0, 12, 0, 0],
      [0,  0, 0, 0]
    ]

    # Act
    answer = dijkstra(adjacency_matrix, 3)

    assert answer == {
        "start_node": 3, 
        "parent_list": [None, None, None, None], 
        "shortest_distances": [float('inf'), float('inf'), float('inf'), 0]
    }
