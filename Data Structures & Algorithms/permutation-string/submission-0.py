class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # L = 0 , R = 2

        if len(s2) < len(s1):
            return False

        s1_count = [0]*26
        sw_count = [0]*26

        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord("a")] += 1
            sw_count[ord(s2[i]) - ord("a")] += 1
        if s1_count == sw_count:
            return True
        R = 0
        for i in range(len(s1), len(s2)):            
          sw_count[ord(s2[i]) - ord("a")] += 1
          sw_count[ord(s2[i-len(s1)]) - ord("a")] -=1
          if s1_count == sw_count:
            return True
        
        return False
            




            


