import unittest

from graph import Graph


class TestGraph(unittest.TestCase):
    def test_outgoing_edges(self):
        graph = Graph()
        graph.add_edge("A", "B", 4)
        graph.add_edge("A", "C", 2)
        graph.add_edge("B", "C", 1)
        self.assertEqual(graph.get_edges("A"), {"B": 4, "C": 2})
        self.assertEqual(graph.get_edges("B"), {"C": 1})

    def test_all_vertices_are_returned(self):
        # Assumes get_vertices returns an iterable, including destination-only nodes.
        graph = Graph()
        graph.add_edge("A", "B", 4)
        vertices = graph.get_vertices()
        self.assertIsNotNone(vertices, "Return the vertices instead of only printing them.")
        self.assertEqual(set(vertices), {"A", "B"})

    def test_clear_and_reuse(self):
        graph = Graph()
        graph.add_edge("A", "B", 4)
        graph.clear()
        self.assertEqual(graph.adj, {})
        graph.add_edge("A", "C", 2)
        self.assertEqual(graph.get_edges("A"), {"C": 2})


if __name__ == "__main__":
    unittest.main()
