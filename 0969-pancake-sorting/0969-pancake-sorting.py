class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = []
        
        while n > 0:
            max_index = arr.index(max(arr[:n]))
            
            if max_index != 0:
                result.append(max_index + 1)
                arr[:max_index + 1] = arr[: max_index + 1][::-1]
            
            result.append(n)
            arr[:n] = arr[:n][::-1]
        
            n -= 1
        
        return result