# Problem: Camelcase Matching - https://leetcode.com/problems/camelcase-matching/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode() 
    
    def insert(self, word, pattern):
        i = 0
        n = len(pattern)
        curr = self.root
        for char in word:
            if i < n and char == pattern[i]:
                i += 1
            elif char.isupper():
                return False
            pos = ord(char.lower()) - ord('a')
            if not curr.children[pos]:
                curr.children[pos] = TrieNode()
            curr = curr.children[pos]
        
        curr.is_end = Trie
        if i == n:
            return True
        
        return False

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        trie = Trie()
        ans = []

        for query in queries:
            if trie.insert(query, pattern):
                ans.append(True)
            else:
                ans.append(False)
        
        return ans

