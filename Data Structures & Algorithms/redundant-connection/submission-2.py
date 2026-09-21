class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        count = len(edges)
        hashmap = defaultdict(list)
        degree = defaultdict(int)
        for node1, node2 in edges:
            hashmap[node1].append(node2)
            hashmap[node2].append(node1)

            degree[node1] += 1
            degree[node2] += 1
        
        visited = set()
        reduant = []
        for edge in edges:
            l, r = edge
            added = False
            if l not in visited:
                added = True
                visited.add(l)
            if r not in visited:
                added = True
                visited.add(r)
            if not added:
                 reduant.append(edge)

        def bfs(hashmap, skip):
            n1, n2 = skip
            queue = deque()
            visit = set()
            queue.append(1)
            visit.add(1)

            while queue:
                val = queue.popleft()
                for n in hashmap[val]:
                    if n1 == val or n2 == val:
                        if n2 == n or n1 == n:
                            continue
                    if n not in visit:
                        queue.append(n)
                        visit.add(n)
            if count != len(visit):
                return False
            else:
                return True

        for i in range(len(reduant) - 1, -1, -1):
            if bfs(hashmap, reduant[i]):
                return reduant[i]

        return -1


        
        
            
