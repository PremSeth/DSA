from sqlite3 import connect
import heapq
from graph import Graph
from priority_queue import minPQ

class dijkstra:
    def __init__(self, graph: Graph, pq: minPQ): 
        self.graph = graph
        self.pq = pq
        self.shortest = {}  # Best cost and predecessor per vertex.
    
    def search(self, start, destination): 
        seen = set()
        self.pq.priority_add(start, 0)
        total_cost = 0
        self.shortest[start] = (0, None)
        if start == destination: 
            return [start]
        while not self.pq.is_empty():
            cost, node = self.pq.next()
            if node in seen:
                continue
            seen.add(node)
            if node == destination:
                self.pq.heap = []
                break
            for connection, new_cost in self.graph.get_edges(node).items():
                if connection not in self.shortest or self.shortest[connection][0] > cost + new_cost: 
                    self.shortest[connection] = (cost + new_cost, node)  # Record the cheaper route.
                self.pq.priority_add(connection, cost+new_cost)
        if not destination in self.shortest: 
            return None
        else: 
            val = destination
            path = []
            while not val == None:  # Follow predecessors to the start.
                path.append(val)
                val = self.shortest[val][1]
        path.reverse()
        return path
    