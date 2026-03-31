class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         lst2 = [] 
         for x in nums:
            if x not in lst2:
                lst2.append(x)
            else:
                return True
         return False