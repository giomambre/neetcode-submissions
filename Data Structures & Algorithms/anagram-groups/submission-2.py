class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mapToList = defaultdict(list)
        
        for i in range(len(strs)):
            mask = [0] * 26

            for j in range(len(strs[i])):
                mask[ord(strs[i][j]) - ord("a")] +=1
            
            mapToList[tuple(mask)].append(strs[i])
        
        return [ lista for lista in mapToList.values() ]
