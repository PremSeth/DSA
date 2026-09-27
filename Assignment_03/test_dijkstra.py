import subprocess
import sys
import unittest
from graph import Graph
from priority_queue import minPQ
from dijkstra import Dijkstra


class TestDijkstra(unittest.TestCase):
    def make_graph(self, edges):
        graph = Graph()
        for start, end, cost in edges:
            graph.add_edge(start, end, cost)
        return graph

    def test_shorter_indirect_path(self):
        graph = self.make_graph([('A', 'B', 10), ('A', 'C', 2), ('C', 'B', 3)])
        self.assertEqual(Dijkstra(graph, minPQ()).search('A', 'B'), ['A', 'C', 'B'])

    def test_unreachable_destination(self):
        # A reachable cycle must not keep the search running forever.
        code = "from graph import Graph; from priority_queue import minPQ; from dijkstra import Dijkstra; g = Graph(); g.add_edge('A', 'B', 1); g.add_edge('B', 'A', 1); g.add_edge('C', 'D', 1); print(Dijkstra(g, minPQ()).search('A', 'D'))"
        result = subprocess.run([sys.executable, '-c', code], capture_output=True, text=True, timeout=2, check=True)
        self.assertEqual(result.stdout.strip(), 'None')

    def test_start_is_destination(self):
        graph = self.make_graph([('A', 'B', 1)])
        self.assertEqual(Dijkstra(graph, minPQ()).search('A', 'A'), ['A'])


if __name__ == '__main__':
    unittest.main()
