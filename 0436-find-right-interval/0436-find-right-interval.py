class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def binarySearch(array, target):
            l, r =  0, len(array) - 1
            
            while l <= r:
                mid = (l + r) // 2
                if array[mid][0] < target:
                    l = mid + 1
                elif array[mid][0] > target:
                    r = mid - 1
                else:
                    return mid
            
            return l
                    
        original = intervals[:]
        intervals.sort(key=lambda x: x[0])
        store = {}
        ans = []
        for interval in intervals:
            index = binarySearch(intervals, interval[1])
            if index < len(intervals):
                store[str(interval)] = intervals[index]
            else:
                store[str(interval)] = -1
                
        for interval in original:
            if store[str(interval)] != -1:
                ans.append(original.index(store[str(interval)]))
            else:
                ans.append(-1)
        
        return ans