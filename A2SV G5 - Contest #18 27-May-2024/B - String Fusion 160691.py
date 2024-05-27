# Problem: B - String Fusion - https://codeforces.com/gym/526229/problem/B

class TrieNode:
    def __init__(self):
        self.children = {}
        self.frequency = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            val = ord(char) - ord('a')
            if val not in curr.children:
                curr.children[val] = TrieNode()
            
            curr.children[val].frequency += 1
            
            curr = curr.children[val]
    
    def search(self, word):
        curr = self.root
        count = 0
        for char in word:
            val = ord(char) - ord('a')
            if val not in curr.children:
                return count
            count += 2 * curr.children[val].frequency
            curr = curr.children[val]
        
        return count


n = int(input())
trie = Trie()
words = []
totalLen = 0
for _ in range(n):
    word = input()
    totalLen += len(word)
    words.append(word)
    trie.insert(word)

count = 2 * n * totalLen

for word in words:
    count -= trie.search(word[::-1])

print(count)

