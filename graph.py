"""
* Name         : graph.py
* Author       : E Wilber
* Created      : 01/27/25
* Module       : 2
* Topic        : 4
* Description  : Graph Program Assignment
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""
from collections import deque
def create_graph():
# Adjacency list representation of graph
    graph = {
        'A': ['D'],
        'B': ['D', 'F'],
        'C': [],
        'D': ['A', 'B', 'G', 'H'],
        'E': ['F', 'G', 'I'],
        'F': ['B', 'E'],
        'G': ['D', 'E'],
        'H': ['D'],
        'I': ['E']
    }
    return graph
def shortest_path(graph, start, end):
# Breadth-First Search finds the shortest path
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        current, path = queue.popleft()

        if current == end:
            return path

        if current not in visited:
            visited.add(current)
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None
def node_with_most_edges(graph):
    return max(graph, key=lambda node: len(graph[node]))
def find_isolated_nodes(graph):
    return [node for node, edges in graph.items() if len(edges) == 0]
def main():
    graph = create_graph()
#Shortest path between A and I
    path = shortest_path(graph, 'A', 'I')
#Node with the most edges
    most_edges_node = node_with_most_edges(graph)
#Isolated nodes
    isolated_nodes = find_isolated_nodes(graph)
# Results
    print("SHORTEST PATH BETWEEN A & I:", path)
    print("NODE WITH THE MOST EDGES:", most_edges_node)
    print("ISOLATED NODES:", isolated_nodes)
if __name__ == "__main__":
    main()
