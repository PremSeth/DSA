from doubly_linked_list import DLL, Node 
class Queue: 
    def __init__(self, val: int) -> None: 
        node = Node(val)
        self.q = DLL(node)
    
    def enqueue(self, data: int) -> None:
        self.q.push_back(Node(data))
        
    def dequeue(self) -> int | None:
        return self.q.pop_front()
        
    def peek(self) -> int | None:
        return self.q.peek_front()

    def is_empty(self) -> bool:
        return self.q.is_empty()
    
       
        
    
    
 

