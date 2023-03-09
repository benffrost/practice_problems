class Trie:

    def __init__(self):
        self.wordend = False
        self.children = defaultdict(Trie)

    def insert(self, word: str) -> None:
        current = self
        for char in word:
            current = current.children[char]
        current.wordend = True

    def search(self, word: str) -> bool:
        current = self
        
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        
        return current.wordend



    def startsWith(self, prefix: str) -> bool:
        current = self
        
        for char in prefix:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)