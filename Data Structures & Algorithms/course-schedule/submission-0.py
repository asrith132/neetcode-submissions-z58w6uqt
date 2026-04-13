class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for c1, c2 in prerequisites:
            indegree[c1] += 1
            adj[c2].append(c1)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        visited = 0
        while q:
            node = q.popleft()
            visited += 1
            for neighbors in adj[node]:
                indegree[neighbors] -= 1
                if indegree[neighbors] == 0:
                    q.append(neighbors)
        return visited == numCourses
            
            