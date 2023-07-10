class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = ""
        
        while word1 and word2:
            if word1 > word2:
                merge += word1[0]
                word1 = word1[1:]
            else:
                merge += word2[0]
                word2 = word2[1:]
        
        merge += word1
        merge += word2
            
        return merge