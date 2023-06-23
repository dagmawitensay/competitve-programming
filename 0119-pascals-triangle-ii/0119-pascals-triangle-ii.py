class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            prevRow = self.getRow(rowIndex - 1)
            temp = []
            for i in range(len(prevRow) - 1):
                temp.append(prevRow[i] + prevRow[i+1])
            return [1] + temp + [1]


        


                