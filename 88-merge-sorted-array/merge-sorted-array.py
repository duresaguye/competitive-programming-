class Solution(object):
    def merge(self, nums1, m, nums2, n):
        seen =0
        while(m < len(nums1)):              
            nums1[m] = nums2[seen]
            seen+=1
            m+=1
        nums1.sort()
        

                    
               
      
        