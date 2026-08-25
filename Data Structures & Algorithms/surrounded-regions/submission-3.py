class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue = deque()
        rows = len(board)
        cols = len(board[0])

        # find all 0s
        for i in range(0, rows):
            for j in range(0, cols):
                if board[i][j] == 'O':
                    queue.append((i, j))
        
        #look through all 0s
        while queue:

            #keep track of the SCC in visited
            i, j = queue.popleft()
            visited = set()
            new_queue = deque()
            new_queue.append((i, j))

            #check
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                edge = True
            else:
                edge = False
            

            visited.add((i, j))
            while new_queue:
                ni, nj = new_queue.popleft()
                directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

                for direction in directions:
                    x, y = direction
                    nx = ni + x
                    ny = nj + y

                    if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == 'O' and (nx, ny) not in visited:
                        if nx == 0 or nx == rows - 1 or ny == 0 or ny == cols - 1:
                            edge = True
                        new_queue.append((nx, ny))
                        visited.add((nx, ny))

            
            if not edge:
                for x, y in visited:
                    board[x][y] = 'X'

        return



            