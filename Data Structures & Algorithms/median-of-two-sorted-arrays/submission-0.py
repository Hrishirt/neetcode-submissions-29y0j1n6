class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sortedArr = nums1 + nums2
        sortedArr.sort()
        l, r = 0, len(sortedArr) - 1 
        while l <= r: 
            m = (l + r) // 2 
            if len(sortedArr) % 2 == 0: 
                r = m + 1 
                return float((sortedArr[m] + sortedArr[r]) / 2)
            else:
                return float(sortedArr[m])