class Solution:
    def bestClosingTime(self, customers: str) -> int:
        yes_no = [0] *(len(customers) + 1)

        for i, val in enumerate(customers):
            if val == 'Y':
                yes_no[i + 1] = 1
        
        total = sum(yes_no)
        prefix_sum = 0
        min_index, min_val = 0, float('inf')

        for i in range(len(customers) + 1):
            if i == 0:
                curr_sum = total
            prefix_sum += yes_no[i]
            curr_sum = (i + 1 + total - 2 * prefix_sum)
            if curr_sum < min_val:
                min_val = curr_sum
                min_index = i
            
        return min_index
