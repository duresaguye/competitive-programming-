class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N =len(nums)
        maxSubArray = float('-inf')
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum+num)
            maxSubArray = max(maxSubArray,current_sum)
        return maxSubArray
    """  
    brute force approch  
        N =len(nums)
        maxSubArray = float('-inf')
        for i in range(N):
            current_sum = 0
            for j in range(i,N):
                current_sum +=nums[j]
                maxSubArray = max(maxSubArray,current_sum)
        return maxSubArray
        """
        
        



    


        

        