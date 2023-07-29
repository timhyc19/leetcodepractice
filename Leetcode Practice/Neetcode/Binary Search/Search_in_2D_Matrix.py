class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        row = 0

        # find row
        while top <= bottom:
            m = (top + bottom) // 2
            if matrix[m][-1] < target:
                top = m + 1
            elif matrix[m][0] > target:
                bottom = m - 1
            else:
                break

        if not (top <= bottom):
            return False
        
        row = (top + bottom) // 2
        l, r = 0, len(matrix[0])
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        
        return False
    