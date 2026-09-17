from __future__ import annotations


class Node:
    def __init__(self, val: int) -> None:
        """
        Creates a node.
        Args:
            val (int): The value to store.
        """
        self.val = val
        self.next: Node | None = None
        self.prev: Node | None = None


class DLL:
    def __init__(self, head: Node | None = None) -> None:
        """
        Creates a doubly linked list.
        Args:
            head (Node | None): The starting node, or None for an empty list.
        """
        self.head = head
        self.tail = head
        self.count = 0 if head is None else 1

    def push_front(self, node: Node) -> None:
        """
        Adds a node to the front.
        Args:
            node (Node): The node to add.
        """
        node.prev = None
        node.next = self.head
        if self.head is None:
            self.tail = node
        else:
            self.head.prev = node
        self.head = node
        self.count += 1

    def push_back(self, node: Node) -> None:
        """
        Adds a node to the back.
        Args:
            node (Node): The node to add.
        """
        node.next = None
        node.prev = self.tail
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.count += 1

    def pop_front(self) -> int | None:
        """
        Removes the front node.
        Returns:
            (int | None): The removed value, or None if empty.
        """
        if self.head is None:
            return None
        node = self.head
        self.head = node.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        node.next = None
        self.count -= 1
        return node.val

    def pop_back(self) -> int | None:
        """
        Removes the back node.
        Returns:
            (int | None): The removed value, or None if empty.
        """
        if self.tail is None:
            return None
        node = self.tail
        self.tail = node.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        node.prev = None
        self.count -= 1
        return node.val

    def peek_front(self) -> int | None:
        """
        Reads the front value.
        Returns:
            (int | None): The front value, or None if empty.
        """
        return None if self.head is None else self.head.val

    def peek_back(self) -> int | None:
        """
        Reads the back value.
        Returns:
            (int | None): The back value, or None if empty.
        """
        return None if self.tail is None else self.tail.val

    def is_empty(self) -> bool:
        """
        Checks whether the list is empty.
        Returns:
            (bool): True if empty, otherwise false.
        """
        return self.head is None

    
