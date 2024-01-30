class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        margenum =nums1+nums2
        margenum.sort()
        median = 0
        n=len(margenum)
        
        if n %2==0:
            median =(margenum[n // 2 - 1] +margenum[n // 2]) / 2
        else:
            median = margenum[n//2]
        return median


        