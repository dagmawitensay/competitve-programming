class Solution:
    def sortSentence(self, s: str) -> str:
        # arr=s.split()
        # ans=[0]*len(arr)
        # for element in arr:
        #     idx=element[-1]
        #     ans[int(idx)-1]=element[:-1]
        # return " ".join(ans)
        arr = s.split()
        arr.sort(key=lambda x: int(x[-1]))
        return " ".join([word[:-1] for word in arr])



