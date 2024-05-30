# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.children = [None] * 2
        self.is_end = True

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, n):
        curr = self.root
        for i in range(32, -1, -1):
            bit = 1 if n & (1 << i) != 0 else 0
            if not curr.children[bit]:
                curr.children[bit] = TrieNode()
            
            curr = curr.children[bit]
        
        curr.is_end = True
    
    def getXor(self, n):
        val = 0
        curr = self.root

        for i in range(32, -1, -1):
            bit = 1 if n & (1 << i) != 0 else 0
            if not curr.children[1 - bit]:
                val &= ~(1 << i)
                curr = curr.children[bit]
            else:
                val |= (1 << i)
                curr = curr.children[1 - bit]
        
        return val



class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        
        for num in nums:
            trie.insert(num)
        
        maxXor = 0
        for num in nums:
            maxXor = max(maxXor, trie.getXor(num))
        
        return maxXor
        