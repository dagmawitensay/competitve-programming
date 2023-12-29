class Solution:
    def smallestNumber(self, num: int) -> int:
        status = False
        num = str(num)
        if len(num) == 1:
            return int(num)
            
        if num[0] == '-':
            status = True
            num = num[1:]
    
        arr = list(map(int, str(num)))
        arr.sort(reverse=status)

        if status:
            return -1 * int("".join(map(str, arr)))
        
        if arr[0] == 0:
            i = 1
            while i < len(arr) and arr[i] == 0:
                i += 1
            
            arr[0], arr[i] = arr[i], arr[0]
        
        return int("".join(map(str, arr)))
