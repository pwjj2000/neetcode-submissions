class PrefixTree:

    def __init__(self):
        self.words = {}

    def insert(self, word: str) -> None:
        d = self.words
        for c in word:  
            if c in d.keys():
                d = d[c]
            else:
                d[c] = {}
                d = d[c]
        d["END"] = True
            
    def search(self, word: str) -> bool:
        d = self.words
        for c in word:
            if c not in d.keys():
                return False
            else:
                d = d[c]
        return "END" in d.keys()
    def startsWith(self, prefix: str) -> bool:
        d = self.words
        for c in prefix:
            if c not in d.keys():
                return False
            else:
                d = d[c]
        return True
        