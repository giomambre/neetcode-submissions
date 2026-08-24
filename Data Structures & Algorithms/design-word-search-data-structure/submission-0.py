
class TreeNode:
    def __init__(self):
        self.childrens = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.childrens:
                curr.childrens[c] = TreeNode()
            curr = curr.childrens[c]
        
        curr.word = True   

    def search(self, word: str) -> bool:
        
        def dfs(j , root):
            cur = root
            for i in range(j,len(word)):
                c = word[i]
                if c == ".":

                    for child in cur.childrens.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if c not in cur.childrens:
                        return False
                    cur = cur.childrens[c]
            return cur.word

        return dfs(0,self.root)
