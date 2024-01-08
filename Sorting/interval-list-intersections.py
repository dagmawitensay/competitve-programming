class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first, second = 0, 0
        ans = []
        n, m = len(firstList), len(secondList)

        while first < n and second < m:
            pair1, pair2 = firstList[first], secondList[second]
            left_val = max(pair1[0], pair2[0])
            right_val = min(pair1[1], pair2[1])
            if right_val >= left_val:
                ans.append([left_val, right_val])
            
            if pair1[1] > pair2[1]:
                second += 1
            else:
                first += 1
        
        return ans