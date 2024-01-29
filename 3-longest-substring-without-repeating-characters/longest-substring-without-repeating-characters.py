class Solution(object):
    def lengthOfLongestSubstring(self, s):
        s_set = set()
        max_len =0
        left = 0
        for char in s: 
            while char in s_set:
                s_set.remove(s[left])
                left+=1
            
            s_set.add(char)
           
            max_len = max(max_len, len(s_set))
    
        return max_len


        
     

       