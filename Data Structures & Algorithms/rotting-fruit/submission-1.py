class Solution:

    from collections import deque


    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        minutes = 0
        fresh_fruits = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    fresh_fruits += 1
                elif grid[i][j]:
                    q.append((i, j))

        while fresh_fruits > 0 and q:
            minutes += 1
            for i in range(len(q)):
                i, j = q.popleft()
                if i + 1 < len(grid) and grid[i+1][j] == 1:
                    q.append((i+1, j))
                    fresh_fruits -= 1
                    grid[i+1][j] = 2
                if i - 1 >= 0 and grid[i-1][j] == 1:
                    q.append((i-1, j))
                    fresh_fruits -= 1
                    grid[i-1][j] = 2
                if j + 1 < len(grid[0]) and grid[i][j+1] == 1:
                    q.append((i, j+1))
                    fresh_fruits -= 1
                    grid[i][j+1] = 2
                if j - 1 >= 0 and grid[i][j-1] == 1:
                    q.append((i, j-1))
                    fresh_fruits -= 1
                    grid[i][j-1] = 2
    
        if fresh_fruits > 0:
            return -1
        return minutes 