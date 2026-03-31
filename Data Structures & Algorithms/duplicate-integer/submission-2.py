class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst = [] 
        for x in nums:
            if x not in lst:
                lst.append(x)
            else:
                return True
        return False