def dijkstra_no_heap(adj_list, num_vertices, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    while len(visited) < len(graph):
        min_node = None
        min_distance = float('inf')
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node
        if min_node is None:
            break  
        visited.add(min_node)
        for neighbor, weight in graph[min_node]:
            if distances[min_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[min_node] + weight
    return distances
def bellman_ford(edges, num_vertices, start):
    distances = [float('inf')] * num_vertices
    distances[start] = 0
    for _ in range(num_vertices - 1):
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            raise ValueError("The graph has a negative loop!")
    return distances
def main():
    print("Shortest Path Algorithms: Bellman-Ford and Dijkstra (no heapq)\n")
    num_vertices = int(input("Enter number of vertices: "))
    num_edges = int(input("Enter number of edges: "))
    print("Enter each edge as: from to weight")
    edges = []
    graph = {i: [] for i in range(num_vertices)}
    for i in range(num_edges):
        u, v, w = map(int, input(f"Edge {i+1}: ").split())
        edges.append((u, v, w))
        graph[u].append((v, w))  
    start_node = int(input("Enter starting vertex: "))
    print("\nBellman-Ford Result ")
    try:
        bf_distances = bellman_ford(edges, num_vertices, start_node)
        for i, d in enumerate(bf_distances):
            print(f"Node {i}: {d if d != float('inf') else 'Unreachable'}")
    except ValueError as e:
        print("Error:", e)
    print("\n Dijkstra Result ")
    dj_distances = dijkstra_no_heap(graph, start_node, num_vertices)
    for i, d in enumerate(dj_distances):
        print(f"Node {i}: {d if d != float('inf') else 'Unreachable'}")
if __name__ == "__main__":
    main()