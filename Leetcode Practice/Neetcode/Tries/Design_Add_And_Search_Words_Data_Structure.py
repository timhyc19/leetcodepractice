class Node():
     def __init__(self):
         self.children = {}
         self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.isWord = True

    def search(self, word: str) -> bool:
        def dfs(node, j):
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in node.children.values():
                        if dfs(child, i + 1): return True
                    return False
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]
            
            return node.isWord
        
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
