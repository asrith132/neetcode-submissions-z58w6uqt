"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        queue = deque([node])
        hashmap = {}
        hashmap[node] = Node(node.val)
        while queue:
            current_node = queue.pop()
            for neighbor in current_node.neighbors:
                if neighbor not in hashmap and neighbor is not None:
                    queue.append(neighbor)
                    hashmap[neighbor] = Node(neighbor.val)
                hashmap[current_node].neighbors.append(hashmap[neighbor])
        return hashmap[node]





