class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.queue) == 0
    
    def enqueue(self, item, priority):
        """Add an item with a given priority"""
        self.queue.append((priority, item))
        # Sort the queue based on priority (lower number = higher priority)
        self.queue.sort(key=lambda x: x[0])
    
    def dequeue(self):
        """Remove and return the highest priority item"""
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        return self.queue.pop(0)[1]
    
    def front(self):
        """Return the highest priority item without removing it"""
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        return self.queue[0][1]
    
    def __len__(self):
        """Return the number of items in the queue"""
        return len(self.queue)
    
    def __str__(self):
        """String representation of the priority queue"""
        return str(self.queue)