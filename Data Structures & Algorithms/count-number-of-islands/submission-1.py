class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands_count = 0
        visited = set()
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                current_element = (i, j)
                if current_element not in visited and grid[i][j] == "1":
                    stack = []
                    stack.append((i, j))
                    while stack:
                        current_i, current_j = stack.pop()
                        visited.add((current_i, current_j))
                        n = (current_i - 1, current_j) 
                        s = (current_i + 1, current_j) 
                        e = (current_i, current_j + 1) 
                        w = (current_i, current_j - 1) 

                        if current_i + 1 < len(grid):
                            if grid[current_i + 1][current_j] == "1" and s not in visited:
                                stack.append(s)
                                visited.add(s)
                                
                        if current_i - 1 >= 0:
                            if grid[current_i - 1][current_j] == "1" and n not in visited:
                                stack.append(n)
                                visited.add(n)
                        
                        if current_j + 1 < len(grid[0]):
                            if grid[current_i][current_j + 1] == "1" and e not in visited:
                                stack.append(e)
                                visited.add(e)

                        if current_j - 1 >= 0:
                            if grid[current_i][current_j - 1] == "1" and w not in visited:
                                stack.append(w)
                                visited.add(w)
                    islands_count += 1
        return islands_count