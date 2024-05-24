# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
        
        curr.is_end = True
    
    def longestWord(self):
        node = self.root
        queue = deque([(node, "")])
        ans = ""

        while queue:
            curr, val = queue.popleft()
            if len(ans) < len(val):
                ans = val
            elif len(ans) == len(val):
                if ans[::-1] > val[::-1]:
                    ans = val

            for key, child in curr.children.items():
                if child.is_end:
                    queue.append((child, key + val))
        
        return ans[::-1]
        



class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        return trie.longestWord()
    
    
        # minWords = []
        # wordSet = set(words)
        # for word in words:
        #     for i in range(len(word)):
        #         if word[:i + 1] not in wordSet:
        #             break
        #     else:
        #         minWords.append(word)
        
        # minWords.sort(key=lambda x: (len(x), x))
        # ans = ""

        # for i in range(len(minWords) - 1, -1, -1):
        #     if i - 1 > 0:
        #         if len(minWords[i]) != len(minWords[i - 1]):
        #             ans = minWords[i]
        #             break
        #     else:
        #         ans = minWords[i]
    
        # return ans

        


        
