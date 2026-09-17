from doubly_linked_list import DLL, Node


class Stack:
    def __init__(self, val: int | None = None) -> None:
        """
        Creates a stack.
        Args:
            val (int | None): The starting value, or None for an empty stack.
        """
        self.stack = DLL(Node(val) if val is not None else None)

    def push(self, item: int) -> None:
        """
        Adds a value to the top.
        Args:
            item (int): The value to add.
        """
        self.stack.push_back(Node(item))

    def pop(self) -> int | None:
        """
        Removes the top value.
        Returns:
            (int | None): The removed value, or None if empty.
        """
        if self.stack.is_empty():
            print("Underflow")
            return None
        return self.stack.pop_back()

    def peek(self) -> int | None:
        """
        Reads the top value without removing it.
        Returns:
            (int | None): The top value, or None if empty.
        """
        if self.stack.is_empty():
            print("empty")
            return None
        return self.stack.peek_back()

    def isEmpty(self) -> bool:
        """
        Checks whether the stack is empty.
        Returns:
            (bool): True if empty, otherwise false.
        """
        return self.stack.is_empty()

    def size(self) -> int:
        """
        Counts the values in the stack.
        Returns:
            (int): The number of values.
        """
        return self.stack.count
