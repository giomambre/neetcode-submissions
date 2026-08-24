class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_1 = {}
        map_2 = {}

        for i in s:
            if i in map_1:
                map_1[i] +=1
            else:
                map_1[i] = 1
        
        for i in t:
            if i in map_2:
                map_2[i] +=1
            else:
                map_2[i] = 1
        
        return map_2 == map_1