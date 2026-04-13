# hashmap has key, linkedlist pairs
# linkedlist contains next, prev, keys, and values
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.current_capacity = 0
        self.hashmap = {}
        self.left_node = Node(-1, -1)
        self.right_node = Node(-3, -3)
        self.left_node.next = self.right_node
        self.right_node.prev = self.left_node
    
    def insert(self, node):
        prev = self.right_node.prev
        node.next = self.right_node
        self.right_node.prev = node
        node.prev = prev
        prev.next = node
    
    def delete(self, node):
        next_node = node.next
        prev_node = node.prev
        prev_node.next = next_node
        next_node.prev = prev_node


    def get(self, key: int) -> int:
        if key in self.hashmap.keys():
            self.delete(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap.keys():
            self.delete(self.hashmap[key])
            self.insert(self.hashmap[key])
            self.hashmap[key].val = value
        else:
            self.current_capacity += 1
            if self.current_capacity > self.max_capacity:
                del self.hashmap[self.left_node.next.key]
                self.delete(self.left_node.next)
            self.hashmap[key] = Node(key, value)
            self.insert(self.hashmap[key])
            
        
        
