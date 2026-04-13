class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.capacity = 0
        self.cache = {}
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left
    
    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        
    def insertNode(self, node):
        prevNode = self.right.prev
        nextNode = self.right

        node.prev = prevNode
        prevNode.next = node

        node.next = nextNode
        nextNode.prev = node

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node is None:
            return -1
        self.removeNode(node)
        self.insertNode(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node is None:
            new_node = Node(key, value)
            self.capacity = self.capacity + 1
            self.insertNode(new_node)
            self.cache[key] = new_node
            if self.capacity > self.max_capacity:
                node_to_remove = self.left.next
                self.cache.pop(node_to_remove.key)
                self.removeNode(node_to_remove)
                self.capacity = self.capacity - 1
        else:
            node.val = value
            self.removeNode(node)
            self.insertNode(node)
