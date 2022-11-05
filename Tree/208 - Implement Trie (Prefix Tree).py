class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        d = self.trie
        for char in word:
            if char not in d:
                d[char] = {}
            d = d[char]
        d["end"] = True

    def search(self, word: str) -> bool:
        c = self.trie
        for char in word:
            if char not in c:
                return False
            c = c[char]
        return "end" in c
        
    def startsWith(self, prefix: str) -> bool:
        c = self.trie
        for char in prefix:
            if char not in c:
                return False
            c = c[char]
        return True