class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.endOfAWord = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.childrens:
                curr.childrens[c] = TrieNode()

            curr = curr.childrens[c]

        curr.endOfAWord = True


    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.childrens:
                return False

            curr = curr.childrens[c]

        return curr.endOfAWord


    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.childrens:
                return False

            curr = curr.childrens[c]

        return True