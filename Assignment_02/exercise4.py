from doubly_linked_list import Node
from stack import Stack

def main():
    """
    Checks bracket matching using a stack; requires paran to be defined.
    Returns:
        (bool): True if the brackets match, otherwise false.
    """
    start = paran[0]
    q = Stack(Node(start))

    for i in paran[1:]: 
        if i == '(':
            q.push(1)
        if i == '{':
            q.push(2)
        if i == '[':
            q.push(3)
        
        if i == ')':
            if not q.pop() == 1: 
                return False
        if i == '}':
            if not q.pop() == 2: 
                return False
        if i == ']':
            if not q.pop() == 3: 
                return False
    
    if q.isEmpty(): 
        return True
    else:
        return False
