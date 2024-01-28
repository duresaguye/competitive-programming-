class Solution:
    def minimumMoves(self, s: str) -> int:
        """i = 0
        moves = 0
        s_len = len(s)
        while i < s_len:

            if s[i] == 'X':
               i += 3
               moves += 1 
            else:
               i += 1

        return moves """
      
        if all(char == 'X' for char in s) and len(s) ==3:
            return 1
        if all(char =='0' for char in s):
            return 0
        right, minmove = 0,0
        while right <len(s):
            if s[right]=='X':
                right +=3
                minmove+=1
            else:
                right+=1

           
        return minmove 
      
        
    

              
               
            
           
            
        
        

        