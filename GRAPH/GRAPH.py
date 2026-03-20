class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2, is_directed=False):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        if not is_directed:
            self.graph[vertex2].append(vertex1)  # For undirected graph

    def display(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")

    def get_vertices(self):
        return list(self.graph.keys())
    
    def get_edges(self):
        for vertex, edges in self.graph.items():
            for edge in edges:
                print(f"{vertex} -> {edge}")

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for edges in self.graph.values():
                if vertex in edges:
                    edges.remove(vertex)

graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')
graph.display()
print("Vertices in the graph:", graph.get_vertices())
print("Edges in the graph:")
graph.get_edges()
graph.remove_vertex('C')
print("Graph after removing vertex C:")
graph.display()
