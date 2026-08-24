class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        L, R = 0, len(height) - 1
        left_max, right_max = height[L], height[R]
        res = 0
        
        while L < R:
            # Chi è il collo di bottiglia? Il lato sinistro o il lato destro?
            if left_max < right_max:
                L += 1
                # Aggiorniamo il massimo a sinistra se abbiamo trovato un muro più alto
                left_max = max(left_max, height[L])
                # L'acqua sopra la colonna corrente è la differenza con il suo massimo
                res += left_max - height[L]
            else:
                R -= 1
                # Aggiorniamo il massimo a destra
                right_max = max(right_max, height[R])
                # L'acqua sopra la colonna corrente è la differenza con il suo massimo
                res += right_max - height[R]
                
        return res