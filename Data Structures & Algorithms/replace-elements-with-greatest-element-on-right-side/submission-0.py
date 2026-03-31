class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = 0 
        while l < len(arr) -1:  
            arr[l] = max(arr[l + 1:len(arr)])
            l+=1 
        arr[-1] = -1 
        return arr