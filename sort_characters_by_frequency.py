class Solution:
    def frequencySort(self, s: str) -> str:
        value_pairs = {}
        for i in s:
            value_pairs[i] = value_pairs.get(i, 0) + 1
        
        paired = list(value_pairs.items())
        paired.sort(key=lambda x: x[1], reverse=True)
        result = ''
        for item, freq in paired:
            result += item * freq
        
        return result
