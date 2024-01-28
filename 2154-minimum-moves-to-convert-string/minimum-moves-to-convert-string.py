class Solution:
    def minimumMoves(self, s: str) -> int:
        i = 0
        moves = 0
        s_len = len(s)
        while i < s_len:

            if s[i] == 'X':
               i += 3
               moves += 1 
            else:
               i += 1

        return moves 
        """
        if all(char == 'X' for char in s):
            return 1
        if all(char =='0' for char in s):
            return 0
        left,right, minmove = 0,1,0
        while right <len(s):
            if s[left]== s[right]:
                right+=1
            elif s[left] != s[right]:
                minmove +=1
                left = right
                right+=1
        return minmove 
        """
        
    

              
               
            
           
            
        
        

        