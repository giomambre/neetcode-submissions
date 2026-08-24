class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""


        for s in strs:
            
            cur_len = len(s)
            encoded += str(cur_len) + "%" + s
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0

        #4%hope3%foo
        while i < len(s):
            cur_len = ""
            while s[i] != "%":
                cur_len += s[i]
                i+=1
            i+=1
            
            decoded.append(s[i:i+int(cur_len)])
            i+= int(cur_len)
        
        return decoded
