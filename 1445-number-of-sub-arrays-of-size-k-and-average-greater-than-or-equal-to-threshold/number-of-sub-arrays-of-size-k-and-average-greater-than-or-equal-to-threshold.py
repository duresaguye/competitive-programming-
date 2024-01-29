class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        num = 0 
        right =0
       
        cursum=0
        while right <len(arr):
            cursum += arr[right]
            if right  >= k-1:
                average = cursum / k
                if average >= threshold:
                    num+=1
                cursum -= arr[right - (k - 1)]
            right +=1
        return num

                
         