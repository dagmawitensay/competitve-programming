class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def helper(s):
            query_store = {i: sum(1 for j in s if j == i) for i in s}
            arr = []

            for k, v in query_store.items():
                arr.append((k, v))
            
            arr.sort(key=lambda x: x[0])

            return arr[0][1]
        
        word_freq_arr = []
        for word in words:
            word_freq_arr.append(helper(word))
        word_freq_arr.sort()

        ans = []
        for query in queries:
            l, r = 0, len(words) - 1
            leftmost_index = None
            check = helper(query)

            while l <= r:
                mid = (l + r) // 2
                middle = word_freq_arr[mid]
                if check < middle:
                    r = mid - 1
                    leftmost_index = mid
                    continue
                else:
                    l = mid + 1
                    continue
            
            if (leftmost_index == None):
                ans.append(0)
                continue
            ans.append(len(word_freq_arr) - leftmost_index)
    
        return ans
            
