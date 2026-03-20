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

    def is_edge(self, vertex1, vertex2):  
        return vertex1 in self.graph[vertex2] or vertex2 in self.graph[vertex1]

    def remove_edge(self, vertex1, vertex2, is_directed=False):
        if self.is_edge(vertex1, vertex2):
            self.graph[vertex1].remove(vertex2)
        if not is_directed and self.is_edge(vertex2, vertex1):
            self.graph[vertex2].remove(vertex1)

    def dfs(self, start, visited=set()):
        if start not in visited:
            visited.add(start)
            print(start, end=' ')

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while len(queue) != 0:
            current = queue.pop(0)
            print(current, end=' ')

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def shortest_path(self, start, end):
        visited = set()
        queue = [(start, [start])]
        visited.add(start)

        while len(queue) != 0:
            current, path = queue.pop(0)

            if current == end:
                print(" -> ".join(path))
                return

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('B', 'E')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')
graph.add_edge('E', 'C')
graph.display()
print("DFS starting from vertex A:")
graph.dfs('A')  
print("\nBFS starting from vertex A:")
graph.bfs('A')
print("The Shortest Path from A to D is:")
graph.shortest_path('A', 'D')
