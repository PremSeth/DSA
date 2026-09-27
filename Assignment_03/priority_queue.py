import heapq

class minPQ:
    def __init__(self):
        self.heap = []  # Lowest priority belongs at the heap root.
        
    def is_empty(self):
        if self.heap:
            return False
        return True

    def priority_add(self, value, priority):
        heapq.heappush(self.heap, (priority, value))
        
    def next(self):
        if self.is_empty():
            return None
        return heapq.heappop(self.heap)

    def adjust_priority(self, value, priority):
        for i,j in enumerate(self.heap):
            if j[1] == value: 
                self.heap[i] = (priority, value)
                heapq.heapify(self.heap)  # Restore heap order.
                break