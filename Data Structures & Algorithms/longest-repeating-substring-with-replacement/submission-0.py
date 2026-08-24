from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # A - Assenza: gestione stringa vuota
        if not s:
            return 0
            
        count_map = defaultdict(int)
        L = 0
        res = 0
        max_freq = 0  # Tiene traccia della massima frequenza vista nella finestra corrente
        
        for R in range(len(s)):
            # 1. Inseriamo il carattere s[R] nella mappa (Nota l'uso di s[R], non R!)
            count_map[s[R]] += 1
            
            # 2. Aggiorniamo la frequenza massima con il carattere appena inserito
            max_freq = max(max_freq, count_map[s[R]])
            
            # Lunghezza della finestra attuale = (R - L + 1)
            # Lettere da cambiare = Finestra attuale - Lettera più frequente
            # Se le lettere da cambiare sono superiori a k, la finestra non è valida!
            while (R - L + 1) - max_freq > k:
                # Stringiamo la finestra da sinistra
                count_map[s[L]] -= 1
                L += 1
                # Nota: Non serve ricalcolare max_freq qui, l'algoritmo si auto-corregge 
                # perché cerchiamo solo finestre che superino il record precedente.
            
            # 3. Ora la finestra è sicuramente valida, aggiorniamo il risultato
            res = max(res, R - L + 1)
            
        return res