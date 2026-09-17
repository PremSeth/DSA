from doubly_linked_list import DLL, Node


class Stack:
    def __init__(self, val: int | None = None) -> None:
        self.stack = DLL(Node(val) if val is not None else None)

    def push(self, item: int) -> None:
        self.stack.push_back(Node(item))

    def pop(self) -> int | None:
        if self.stack.is_empty():
            print("Underflow")
            return None
        return self.stack.pop_back()

    def peek(self) -> int | None:
        if self.stack.is_empty():
            print("empty")
            return None
        return self.stack.peek_back()

    def isEmpty(self) -> bool:
        return self.stack.is_empty()

    def size(self) -> int:
        return self.stack.count
