class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0

        bambino_ptr = 0
        biscotto_ptr = 0
        while bambino_ptr < len(g) and biscotto_ptr < len(s):
        # Se il biscotto soddisfa il bambino
            if s[biscotto_ptr] >= g[bambino_ptr]:
            # Passiamo al prossimo bambino (questo è soddisfatto)
                bambino_ptr += 1
        
        # In ogni caso, passiamo al prossimo biscotto
            biscotto_ptr += 1

        return bambino_ptr