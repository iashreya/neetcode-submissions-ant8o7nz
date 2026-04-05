class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}  # {key: pointer}
        self.start = None
        self.end = None
        self.total = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
            
        node = self.cache[key]
        self.move_front(node)
        return self.start.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.move_front(node)
        else:
            if not self.has_capacity():
                node = self.remove_from_end()
                del self.cache[node.key]
    
            node = self.add_to_front(key, value)
            self.cache[key] = node
            self.total += 1

    def has_capacity(self):
        return self.total < self.capacity

    def add_to_front(self, key, value):
        node = self.Node(key, value)
        node.prev = None
        if self.start:
            self.start.prev = node
        else:
            self.end = node
        node.next = self.start
        self.start = node
        return node

    def remove_from_end(self):
        if not self.end:
            return None
        
        node = self.end
        if self.start == self.end:
            self.start = None
            self.end = None
        else:
            self.end = node.prev
            self.end.next = None
        
        return node



    def move_front(self, node):
        # If pointer is already at start
        if node == self.start:
            return

        # Detach node
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev 

        # If pointer is at the end
        if node == self.end:
            self.end = node.prev

        # Move to the front
        node.prev = None
        node.next = self.start
        self.start.prev = node
        self.start = node

    class Node:
        def __init__(self, key, val, next=None, prev=None):
            self.key = key
            self.val = val
            self.next = next
            self.prev = prev

    
