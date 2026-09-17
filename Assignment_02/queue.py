from doubly_linked_list import DLL, Node 
class Queue: 
    def __init__(self, val: int) -> None: 
        """
        Creates a queue.
        Args:
            val (int): The starting value.
        """
        node = Node(val)
        self.q = DLL(node)
    
    def enqueue(self, data: int) -> None:
        """
        Adds a value to the back.
        Args:
            data (int): The value to add.
        """
        self.q.push_back(Node(data))
        
    def dequeue(self) -> int | None:
        """
        Removes the front value.
        Returns:
            (int | None): The removed value, or None if empty.
        """
        return self.q.pop_front()
        
    def peek(self) -> int | None:
        """
        Reads the front value without removing it.
        Returns:
            (int | None): The front value, or None if empty.
        """
        return self.q.peek_front()

    def is_empty(self) -> bool:
        """
        Checks whether the queue is empty.
        Returns:
            (bool): True if empty, otherwise false.
        """
        return self.q.is_empty()
    
       
        
    
    
 
