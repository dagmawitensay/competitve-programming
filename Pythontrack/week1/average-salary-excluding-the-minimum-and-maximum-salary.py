class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        total = 0
        count = 0

        for val in salary:
            if val != min_salary and val != max_salary:
                count += 1
                total += val
        
        return total / count
        