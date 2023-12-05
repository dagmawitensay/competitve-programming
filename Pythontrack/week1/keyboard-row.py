class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keybords = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        ans = []
        for word in words:
            word_set = set(word.lower())
            if word_set.issubset(keybords[0]) or word_set.issubset(keybords[1]) or word_set.issubset(keybords[2]):
                ans.append(word)


        return ans
