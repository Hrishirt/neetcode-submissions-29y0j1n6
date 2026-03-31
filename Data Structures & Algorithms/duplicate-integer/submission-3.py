class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst = [] 
        for x in nums:
            if x in lst:
                return True
            else:
                lst.append(x)
        return False