class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        arr = [[0 for _ in range(cols)] for _ in range(rows)]
        visited = set()


        def dfs(cordinate):
            x, y = cordinate
            actual_val = matrix[x][y]
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            max_val = 0
            for cx, cy in directions:
                nx = x + cx
                ny = y + cy
                if 0 <= nx < rows and 0 <= ny < cols and actual_val < matrix[nx][ny]:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        new_val = dfs((nx, ny)) + 1
                    else:
                        new_val = arr[nx][ny] + 1
                    
                    max_val = max(new_val, max_val)

            arr[x][y] = max_val
            return max_val
        


        for i in range(0, rows):
            for j in range(0, cols):
                if (i, j) not in visited:
                    visited.add((i, j))
                    dfs((i, j))

        res = 0
        for i in range(0, rows):
            for j in range(0, cols):
                res = max(res, arr[i][j])

        return res + 1

                



            
