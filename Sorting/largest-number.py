class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        snums=list(map(str, nums))
        snums.sort(key=lambda x:x[0],reverse=True)

        for i in range(len(snums)):
            for j in range(i+1,len(snums)):
                if snums[i][0]==snums[j][0]:
                    if int(snums[i]+snums[j]) <int(snums[j]+snums[i]):
                        snums[i],snums[j]=snums[j],snums[i]

        
        return str(int("".join(snums)))




