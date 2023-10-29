class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = [0] * len(queries)
        
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])
        
        for i, query in enumerate(queries):
            ans[i] = prefix[query[1] + 1] - prefix[query[0]]
        
        return ans