class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        
        for w in strs:
            mask = [0]*26

            for s in w:
                mask[ord(s)-ord('a')]+=1
            map[str(mask)].append(w)
        
        res = []
        for k in map.keys():
            tmp = []
            for v in map[str(k)]:
                tmp.append(v)
            res.append(tmp)
        return res