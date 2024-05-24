# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            val = ord(char) - ord('a')
            if not curr.children[val]:
                curr.children[val] = TrieNode()
            curr = curr.children[val]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            for i in range(index, len(word)):
                char = word[i]
                idx = ord(char) - ord('a')
                if char == ".":
                    for child in node.children:
                        if child and dfs(i + 1, child):
                            return True
                    return False
                else:
                    if not node.children[idx]:
                        return False
                
                node = node.children[idx]
            
            return node.is_end
        
        return dfs(0, self.root)
        
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)