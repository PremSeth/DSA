import unittest

from doubly_linked_list import DLL, Node
from queue import Queue
from stack import Stack


class TestDLL(unittest.TestCase):
    def test_push_front(self) -> None:
        """Checks adding a node to the front."""
        linked_list = DLL(Node(2))
        linked_list.push_front(Node(1))
        self.assertEqual(linked_list.peek_front(), 1)

    def test_push_back(self) -> None:
        """Checks adding a node to the back."""
        linked_list = DLL(Node(1))
        linked_list.push_back(Node(2))
        self.assertEqual(linked_list.peek_back(), 2)

    def test_pop_front(self) -> None:
        """Checks front removal and empty-list handling."""
        linked_list = DLL(Node(1))
        linked_list.push_back(Node(2))
        self.assertEqual(linked_list.pop_front(), 1)
        self.assertEqual(linked_list.peek_front(), 2)
        self.assertEqual(linked_list.count, 1)
        self.assertIsNotNone(linked_list.head)
        assert linked_list.head is not None
        self.assertIsNone(linked_list.head.prev)
        self.assertEqual(linked_list.pop_front(), 2)
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)
        self.assertIsNone(linked_list.pop_front())
        self.assertEqual(linked_list.count, 0)

    def test_pop_back(self) -> None:
        """Checks back removal and empty-list handling."""
        linked_list = DLL(Node(1))
        linked_list.push_back(Node(2))
        self.assertEqual(linked_list.pop_back(), 2)
        self.assertEqual(linked_list.peek_back(), 1)
        self.assertEqual(linked_list.count, 1)
        self.assertIsNotNone(linked_list.tail)
        assert linked_list.tail is not None
        self.assertIsNone(linked_list.tail.next)
        self.assertEqual(linked_list.pop_back(), 1)
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)
        self.assertIsNone(linked_list.pop_back())
        self.assertEqual(linked_list.count, 0)

    def test_peek_front(self) -> None:
        """Checks reading the front value."""
        linked_list = DLL(Node(1))
        linked_list.push_back(Node(2))
        self.assertEqual(linked_list.peek_front(), 1)

    def test_peek_back(self) -> None:
        """Checks reading the back value."""
        linked_list = DLL(Node(1))
        linked_list.push_back(Node(2))
        self.assertEqual(linked_list.peek_back(), 2)

    def test_is_empty(self) -> None:
        """Checks whether the list is empty."""
        linked_list = DLL()
        self.assertTrue(linked_list.is_empty())
        linked_list.push_front(Node(1))
        self.assertFalse(linked_list.is_empty())


class TestStack(unittest.TestCase):
    def test_push(self) -> None:
        """Checks pushing a value."""
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.size(), 1)

    def test_pop(self) -> None:
        """Checks last-in, first-out removal and reuse."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.size(), 0)
        self.assertTrue(stack.isEmpty())
        stack.push(3)
        self.assertEqual(stack.pop(), 3)

    def test_peek(self) -> None:
        """Checks that peek does not remove the top value."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.size(), 2)

    def test_is_empty(self) -> None:
        """Checks whether the stack is empty."""
        stack = Stack()
        self.assertTrue(stack.isEmpty())
        stack.push(1)
        self.assertFalse(stack.isEmpty())

    def test_size(self) -> None:
        """Checks the size after pushes and pops."""
        stack = Stack(0)
        self.assertEqual(stack.size(), 1)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.size(), 3)
        stack.pop()
        self.assertEqual(stack.size(), 2)


class TestQueue(unittest.TestCase):
    def test_enqueue(self) -> None:
        """Checks enqueue order and reuse."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        queue.enqueue(4)
        self.assertEqual(queue.peek(), 4)
        self.assertFalse(queue.is_empty())

    def test_dequeue(self) -> None:
        """Checks first-in, first-out removal and an empty queue."""
        queue = Queue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.peek(), 2)
        self.assertEqual(queue.dequeue(), 2)
        self.assertTrue(queue.is_empty())
        self.assertIsNone(queue.dequeue())
        self.assertTrue(queue.is_empty())

    def test_peek(self) -> None:
        """Checks that peek does not remove the front value."""
        queue = Queue(1)
        queue.enqueue(2)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.peek(), 2)
        queue.dequeue()
        self.assertIsNone(queue.peek())

    def test_is_empty(self) -> None:
        """Checks whether the queue is empty."""
        queue = Queue(0)
        self.assertFalse(queue.is_empty())
        queue.dequeue()
        self.assertTrue(queue.is_empty())
        queue.enqueue(0)
        self.assertFalse(queue.is_empty())


def main() -> None:
    """Runs all unit tests."""
    unittest.main()


if __name__ == "__main__":
    main()
