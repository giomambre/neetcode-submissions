class Solution:

    def encode(self, strs: List[str]) -> str:

        msg = ""

        for s in strs:
            msg = msg + (str(len(s)) +"%" + s) 
       # print(msg)
        return msg

    def decode(self, s: str) -> List[str]:
        
        res = []

        cnt ,i  = 0 , 0
        while i < len(s):
            tmp = ""

            while s[i] != "%":
                tmp += s[i]
                i+=1
            cnt = int(tmp)
            res.append(s[(i+1):(i + cnt + 1)])
    
            i+= cnt + 1
        
        return res