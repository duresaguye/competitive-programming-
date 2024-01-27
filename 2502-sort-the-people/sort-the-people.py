class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Selection sorting
        for i in range(len(heights)):
            minpos = i
            for j in range(i +1 ,len(heights)):  
                if heights[j] > heights[minpos]:
                    minpos = j

            # Swap the values
            heights[i], heights[minpos] = heights[minpos], heights[i]
            names[i], names[minpos] = names[minpos], names[i]

        return names
            

        """#optimal solutions 
        person_info = list(zip(names,heights))
        sorted_person_info = sorted(person_info, key=lambda x:x[1] ,reverse=True )
        # now we have to extrcate the names
        sorted_name = (name for name, _ in sorted_person_info )
       
        return sorted_name

        
        using bubble sorting
        n = len(heights)
        for i in range(n):
            for j in range(0, n-i-1):

                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]
        return names
        """