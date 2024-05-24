# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            val = ord(char) - ord('a')
            if not curr.children[val]:
                curr.children[val] = TrieNode()
            
            curr = curr.children[val]
        curr.is_end = True
    
    def minWord(self, word: str) -> str:
        curr = self.root
        if not curr.children[ord(word[0]) - ord('a')]:
            return word

        res = ""
        for char in word:
            val = ord(char) - ord('a')
            if curr.is_end:
                return res
            if not curr.children[val]:
                if curr.is_end:
                    return res
                return word
            curr = curr.children[val]
            res += char

        return res

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        ans = []
        for word in sentence.split():
            ans.append(trie.minWord(word))
        
        return " ".join(ans)
