class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        cursum,L=0, 0
        for R in range(len(nums)):
            if cursum < 0:
                cursum =0
                L=R
            cursum +=nums[R]
            if cursum > maxsum:
                maxsum =cursum
        return maxsum
    #optimal soultion using kadane's algo
        """max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1,len(nums)):
            current_sum = max(nums[i],current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum"""
    #using sliding windows 

    



    """#brute force approche
        max_subarray = float('-inf')
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i,len(nums)):
                current_sum +=nums[j]
                max_subarray = max(max_subarray,current_sum)
    """
        
        


      