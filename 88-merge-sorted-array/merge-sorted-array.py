class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i,j,seen=m-1,n-1,m+n-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[seen]=nums1[i]
                i-=1
            else:
                nums1[seen]=nums2[j]
                j-=1
            seen-=1
        while j>=0:
            nums1[seen]=nums2[j]
            j-=1
            seen-=1

        



            
            

       

                    
               
      
        