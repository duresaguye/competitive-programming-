from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct_max = set()

        for num in nums:
            distinct_max.add(num)
            
            # Keep the set size limited to 3
            if len(distinct_max) > 3:
                distinct_max.remove(min(distinct_max))

        # If there are at least 3 distinct maximum numbers, return the third one
        if len(distinct_max) >= 3:
            return min(distinct_max)
        # Otherwise, return the maximum number
        else:
            return max(distinct_max)
