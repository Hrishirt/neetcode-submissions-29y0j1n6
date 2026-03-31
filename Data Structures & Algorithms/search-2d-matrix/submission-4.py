class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1 
        while top <= bot: 
            mrow = (top + bot) // 2 
            if target < matrix[mrow][0]: 
                bot = mrow - 1 
            elif target > matrix[mrow][-1]: 
                top = mrow + 1 
            else:
                break 
        if top > bot:
            return False 
        l, r = 0, COLS - 1 
        while l <= r: 
            m = (l + r) // 2 
            if matrix[mrow][m] > target:
                r = m - 1 
            elif matrix[mrow][m] < target: 
                l = m + 1 
            else:
                return True 
        return False
