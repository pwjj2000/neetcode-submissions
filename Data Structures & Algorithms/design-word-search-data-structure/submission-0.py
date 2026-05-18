class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.words = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.words
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True
    def search(self, word: str) -> bool:
        curr = self.words
        def dfs(i, c):
            if i == len(word):
                return c.end
            if word[i] == '.':
                for child in c.children:
                    if dfs(i+1, c.children[child]):
                        return True
            elif word[i] not in c.children:
                return False
            else:
                return dfs(i+1, c.children[word[i]])
            return False
        return dfs(0, curr)