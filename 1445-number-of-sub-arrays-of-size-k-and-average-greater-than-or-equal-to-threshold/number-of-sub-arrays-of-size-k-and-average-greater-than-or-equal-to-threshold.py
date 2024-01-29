class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0 
        right =0
        cursum=0
        left =0
        while right <len(arr):
            cursum += arr[right]
            if right  >= k-1:
                average = cursum / k
                if average >= threshold:
                    res+=1
                cursum -= arr[left]
                left+=1
            right +=1
        return res

                
         