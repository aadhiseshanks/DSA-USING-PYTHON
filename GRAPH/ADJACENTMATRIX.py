class GraphMatrix:
    def __init__(self):
        self.vertices = []
        self.matrix = []

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            size = len(self.vertices)

            # Add new row
            self.matrix.append([0] * size)

            # Add new column to existing rows
            for row in self.matrix:
                if len(row) < size:
                    row.append(0)

    def add_edge(self, v1, v2, is_directed=False):
        self.add_vertex(v1)
        self.add_vertex(v2)

        i = self.vertices.index(v1)
        j = self.vertices.index(v2)

        self.matrix[i][j] = 1
        if not is_directed:
            self.matrix[j][i] = 1

    def display(self):
        print("Adjacency Matrix:")
        print("  ", self.vertices)
        for i in range(len(self.matrix)):
            print(self.vertices[i], self.matrix[i])

    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == 1:
                    print(f"{self.vertices[i]} -> {self.vertices[j]}")

    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            index = self.vertices.index(vertex)

            # Remove vertex
            self.vertices.pop(index)

            # Remove row
            self.matrix.pop(index)

            # Remove column
            for row in self.matrix:
                row.pop(index)

    def is_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            i = self.vertices.index(v1)
            j = self.vertices.index(v2)
            return self.matrix[i][j] == 1
        return False

    def remove_edge(self, v1, v2, is_directed=False):
        if self.is_edge(v1, v2):
            i = self.vertices.index(v1)
            j = self.vertices.index(v2)
            self.matrix[i][j] = 0

        if not is_directed and self.is_edge(v2, v1):
            i = self.vertices.index(v2)
            j = self.vertices.index(v1)
            self.matrix[i][j] = 0


# Example usage
graph = GraphMatrix()
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

print("Is there an edge between A and B?", graph.is_edge('A', 'B'))

graph.remove_edge('A', 'B')
print("Is there an edge between A and B now?", graph.is_edge('A', 'B'))

graph.display()
