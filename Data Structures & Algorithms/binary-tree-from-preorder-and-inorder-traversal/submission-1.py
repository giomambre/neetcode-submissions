class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Hash Map per trovare l'indice di qualsiasi valore in inorder in O(1)
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        # Puntatore per sapere quale elemento di preorder stiamo usando come radice
        self.pre_idx = 0
        
        def helper(in_left, in_right):
            # Caso base: se i puntatori si incrociano, non ci sono più nodi in questa porzione
            if in_left > in_right:
                return None
                
            # 1. Il primo elemento disponibile in preorder è la nostra radice
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            
            # Avanziamo il puntatore del preorder per la prossima chiamata ricorsiva
            self.pre_idx += 1
            
            # 2. Troviamo dove si trova questa radice nell'inorder per spaccare l'array
            mid_idx = inorder_map[root_val]
            
            # 3. Costruiamo ricorsivamente i sottoalberi
            # Sottoalbero sinistro: prende la porzione a sinistra di mid_idx
            root.left = helper(in_left, mid_idx - 1)
            
            # Sottoalbero destro: prende la porzione a destra di mid_idx
            root.right = helper(mid_idx + 1, in_right)
            
            return root
            
        return helper(0, len(inorder) - 1)