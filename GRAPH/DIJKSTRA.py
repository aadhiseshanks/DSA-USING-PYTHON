import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2, cost, is_directed=False):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append([vertex2, cost])
        if not is_directed:
            self.graph[vertex2].append([vertex1, cost])

    def dijsktra(self, start):
        if start not in self.graph:
            print(f"Vertex {start} does not exist in the graph.")
            return {}
        
        distance = {item: float('inf') for item in self.graph}
        distance[start] = 0
        queue = [(0, start)]

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_distance > distance[current_node]:
                continue

            for node, weight in self.graph[current_node]:
                new_distance = current_distance + weight
                if new_distance < distance[node]:
                    distance[node] = new_distance
                    heapq.heappush(queue, (new_distance, node))

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

print(graph.dijsktra('A'))
