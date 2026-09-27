class Graph:
    '''
    A data structure to represent a collection of nodes  
    '''
    def __init__(self):
        self.adj = {}  # Source vertex -> outgoing edges.
    
    def get_vertices(self):
        seen = set()
        for value in self.adj:
            seen.add(value)
            for connections in self.adj[value]:
                seen.add(connections[1])
        return list(seen)
        
    def add_edge(self, start: str, end: str, cost: str):
        self.adj[start] = self.adj.get(start, [])
        self.adj[start].append((cost, end))
        
    def get_edges(self, start: str):
        edges = {}
        if start in self.adj:
            for edge in self.adj[start]: 
                edges[edge[1]] = edge[0]  # Map each neighbor to its cost.
        return edges    
    
    def clear(self):
        self.adj = {}
