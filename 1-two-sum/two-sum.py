class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_index = [(num, idx) for idx, num in enumerate(nums)]
        nums_with_index.sort()

        left, right = 0, len(nums) - 1

        while left < right:
            current_sum = nums_with_index[left][0] + nums_with_index[right][0]
            if current_sum == target:
                return [nums_with_index[left][1], nums_with_index[right][1]]
            elif current_sum > target:
                right -= 1
            else:
                left += 1

        """for i in range(len(nums)):
            for j in range(1,len(nums)):
                if (i != j):
                   if nums[i]+nums[j]==target:
                       return [i,j]
        """
        


        
         
        
    
        
