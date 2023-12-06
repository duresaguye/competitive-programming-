class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic = {}
        hashmap = {}

        # Fix the indentation of the first for loop
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1

        # Fix the variable name typo (hshamap to hashmap) and the indentation of the second for loop
        for d in t:
            if d in hashmap:
                hashmap[d] += 1
            else:
                hashmap[d] = 1

        return hashmap == dic


    """
       is this one way of checking if the string is anagram or not 
       by sorting both of them and checking if the are equal after sorting     
        return sorted(s) == sorted(t)"""

     
       