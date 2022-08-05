class Trie:
    def __init__(self):
        self.children= {}
        self.word = False

class WordDictionary:
    

    def __init__(self):
        self.root = Trie()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        
        for w in word:
            if w not in cur.children:
                cur.children[w] = Trie()
            cur = cur.children[w]
            
        cur.word = True
    def search(self, word: str) -> bool:
        
        def dfs(index , root):
            cur = root

            for i in range(index , len(word)):
                w = word[i]

                if w == ".":
                    for c in cur.children.values():
                        if dfs(i + 1 , c):
                            return True
                        return False

                else:
                    if w not in cur.children:
                        return False
                    cur = cur.children[w]
                    
            return cur.word
        
        return dfs(0 , self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
