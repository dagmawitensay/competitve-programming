class Solution(object):
    def sortSentence(self,s):
        words=s.split(" ")
        original_text=""
        for i in range(1,len(words)+1):
            for word in words:
                if int(word[len(word)-1])==i:
                    original_text+=word[:len(word)-1]
                    if i!=len(words):
                        original_text+=" "
        return original_text


        
