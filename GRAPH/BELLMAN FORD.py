class Graph:
    def __init__(self):
        self.graph = {}
        self.edges = []  # store edges separately for Bellman-Ford

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2, cost, is_directed=False):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.graph[vertex1].append([vertex2, cost])
        self.edges.append((vertex1, vertex2, cost))

        if not is_directed:
            self.graph[vertex2].append([vertex1, cost])
            self.edges.append((vertex2, vertex1, cost))

    def bellman_ford(self, start):
        if start not in self.graph:
            print(f"Vertex {start} does not exist in the graph.")
            return {}

        # Step 1: Initialize distances
        distance = {v: float('inf') for v in self.graph}
        distance[start] = 0

        vertices = list(self.graph.keys())

        # Step 2: Relax edges |V| - 1 times
        for _ in range(len(vertices) - 1):
            for u, v, w in self.edges:
                if distance[u] != float('inf') and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

        # Step 3: Check for negative weight cycles
        for u, v, w in self.edges:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                print("Graph contains a negative weight cycle")
                return None

        return distance

graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'D', 4)
graph.add_edge('A', 'F', 7)
graph.add_edge('B', 'C', 3)
graph.add_edge('C', 'D', 5)
graph.add_edge('C', 'E', 4)
graph.add_edge('C', 'H', 5)
graph.add_edge('D', 'I', 3)
graph.add_edge('D', 'G', 2)
graph.add_edge('H', 'G', 1)

print(graph.bellman_ford('A'))
