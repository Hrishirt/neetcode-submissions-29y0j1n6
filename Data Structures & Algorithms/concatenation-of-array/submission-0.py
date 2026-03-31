class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lst = []
        for x in nums:
            lst.append(x)
        
        lst2 = nums + lst 
        return lst2 