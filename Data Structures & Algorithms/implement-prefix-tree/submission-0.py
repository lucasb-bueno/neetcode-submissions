class TrieNode:
    def __init__(self):
        self.childreen = {}
        self.word = False 

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.childreen:
                curr.childreen[c] = TrieNode()
            curr = curr.childreen[c]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.childreen:
                return False
            curr = curr.childreen[c]
        return curr.word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.childreen:
                return False
            curr = curr.childreen[c]
        return True
        