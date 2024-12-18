from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()

    def add_edge(self, u, v, weight=1):
        self.graph[u].append((v, weight))
        self.vertices.add(u)
        self.vertices.add(v)

    def remove_edge(self, u, v):
        self.graph[u] = [edge for edge in self.graph[u] if edge[0] != v]

    def has_edge(self, u, v):
        return any(edge[0] == v for edge in self.graph[u])

    def get_neighbors(self, vertex):
        return self.graph[vertex]

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0
        
        unvisited = list(self.vertices)
        
        while unvisited:
            current = min(unvisited, key=lambda vertex: distances[vertex])
            
            if distances[current] == float('infinity'):
                break
            
            for neighbor, weight in self.graph[current]:
                distance = distances[current] + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
            
            unvisited.remove(current)
        
        return distances

    def depth_first_search(self, start, visited=None):
        if visited is None:
            visited = set()
        
        visited.add(start)
        
        for neighbor, _ in self.graph[start]:
            if neighbor not in visited:
                self.depth_first_search(neighbor, visited)
        
        return visited

    def breadth_first_search(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        
        while queue:
            vertex = queue.pop(0)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return visited