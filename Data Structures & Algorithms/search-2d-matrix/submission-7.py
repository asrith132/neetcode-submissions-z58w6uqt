class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        column = 0
        while top <= bottom:
            m_col = (top + bottom) // 2 
            if (m_col == len(matrix) - 1):
                column = m_col
                break 
            if (matrix[m_col][0] < target):
                top = m_col + 1
                if (top < len(matrix)):
                    if (target < matrix[top][0]):
                        column = m_col
                        break
            elif (matrix[m_col][0] > target):
                bottom = m_col - 1
                if (bottom >= 0):
                    if (target > matrix[bottom][0]):
                        column = bottom
                        break
            else:
                column = m_col
                break

        l, r = 0, len(matrix[column]) - 1
        
        while l <= r:
            m = (l + r) // 2 
            if matrix[column][m] > target:
                r = m - 1
            elif matrix[column][m] < target:
                l = m + 1
            else:
                return True
        return False
