class Trie:

    def __init__(self):
        self.T = {}

    def insert(self, word: str) -> None:
        node = self.T
        for c in word:
            if c not in node: node[c] = {}
            node = node[c]
        node['#'] = word

    def search(self, word: str) -> bool:
        node = self.T
        for c in word:
            if c not in node: return False
            node = node[c]
        return '#' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.T
        for c in prefix:
            if c not in node: return False
            node = node[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)