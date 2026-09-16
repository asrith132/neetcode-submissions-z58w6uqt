class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def bfs(i, j):
            count = 1
            queue = deque()
            queue.append((i, j))
            while queue:
                x, y = queue.popleft()
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] == 1:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
                        count += 1
            
            return count

        
        res = 0
        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    val = bfs(i, j)
                    res = max(val, res)

        return res