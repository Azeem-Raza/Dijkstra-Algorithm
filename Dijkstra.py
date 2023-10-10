#Generate adjacency lists of 10 nodes as the following figure. 
#Write a Python function which converts the adjacency lists into adjacency matrix. 
#Apply Dijkstra algorithm for the adjacency matrix and output the shortest distance from Node 𝑋
#to all other nodes, where
#X ='A'+lastDigitofYourID. E.g., if your ID is e2301234 then your program outputs Node 𝐸's result.
import random
import numpy as np
import heapq

# Function to generate an empty graph with 'num_nodes' nodes
def generate_graph(num_nodes):
    graph = [[] for _ in range(num_nodes)]
    return graph

# Function to add a directed edge with a specified weight from 'source' to 'destination'
def add_directed_edge(graph, source, destination, weight):
    graph[source].append((destination, weight))

# Function to add an undirected edge (two directed edges with the same weight) between 'node1' and 'node2'
def add_undirected_edge(graph, node1, node2, weight):
    add_directed_edge(graph, node1, node2, weight)
    add_directed_edge(graph, node2, node1, weight)

# Function to convert a graph to an adjacency matrix
def graph_to_adjacency_matrix(graph):
    num_nodes = len(graph)
    adj_matrix = np.inf * np.ones((num_nodes, num_nodes))

# Populate the adjacency matrix with edge weights
    for u, edges in enumerate(graph):
        for v, weight in edges:
            adj_matrix[u][v] = weight
# Set the diagonal elements to 0
    np.fill_diagonal(adj_matrix, 0)
    return adj_matrix

# Function to find the shortest distances from a 'start_node' to all other nodes using Dijkstra's algorithm
def find_shortest_distances(adj_matrix, start_node):
    num_nodes = len(adj_matrix)
    distances = np.inf * np.ones(num_nodes)
    visited = [False] * num_nodes
    distances[start_node] = 0

    min_heap = [(0, start_node)]

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        if visited[current_node]:
            continue

        visited[current_node] = True
# Explore neighbors of the current node
        for neighbor in range(num_nodes):
            if not visited[neighbor] and adj_matrix[current_node][neighbor] != np.inf:
                alt = current_distance + adj_matrix[current_node][neighbor]

                if alt < distances[neighbor]:
                    distances[neighbor] = alt
                    heapq.heappush(min_heap, (alt, neighbor))

    return distances
# Main function to execute the program
def main():
    student_number = int(input("Enter your student number (Numbers only): "))
    random.seed(student_number)

    num_nodes = 11
    graph = generate_graph(num_nodes)
# Define the graph structure by adding edges
    add_undirected_edge(graph, 0, 1, 3)  # A to B
    add_undirected_edge(graph, 1, 7, 1)  # B to H
    add_undirected_edge(graph, 0, 6, 3)  # A to G
    add_undirected_edge(graph, 0, 3, 7)  # A to D
    add_undirected_edge(graph, 7, 6, 1)  # H to G
    add_directed_edge(graph, 3, 2, 1)  # D to C
    add_directed_edge(graph, 3, 9, 3)  # D to S
    add_directed_edge(graph, 2, 8, 8)  # C to G
    add_directed_edge(graph, 8, 9, 9)  # C to S
    add_directed_edge(graph, 6, 9, 4)  # G to S
    add_directed_edge(graph, 3, 4, 2)  # D to E
    add_directed_edge(graph, 4, 5, 6)  # E to F
    add_directed_edge(graph, 9, 10, 2)  # S to T
    add_directed_edge(graph, 4, 10, 1)  # E to T

    adj_matrix = graph_to_adjacency_matrix(graph)

    last_digit_of_id = student_number % 10
    start_node = last_digit_of_id

    shortest_distances = find_shortest_distances(adj_matrix, start_node)
 # Display the shortest distances from the start node to all other nodes
    for i, distance in enumerate(shortest_distances):
        if i != start_node and chr(i + ord('A')) != 'I':
            node_label = chr(start_node + ord('A'))
            if i == 9:
                print(f"Shortest distance from Node {node_label} to Node S: {distance}")
            elif i == 10:
                print(f"Shortest distance from Node {node_label} to Node T: {distance}")
            else:
                print(f"Shortest distance from Node {node_label} to Node {chr(i + ord('A'))}: {distance}")

if __name__ == "__main__":
    main()
