class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target < row[0]:
                return False
            if target > row[len(row) - 1]:
                continue
            else:
                l, r = 0, len(row) - 1
                while l <= r:
                    k = (l + r) // 2 
                    if row[k] == target or row[l] == target or row[r] == target:
                        return True 
                    if target > row[k]:
                        l = k + 1 
                    else:
                        r = k -1 
        return False