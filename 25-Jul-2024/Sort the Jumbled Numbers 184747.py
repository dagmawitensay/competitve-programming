# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

from functools import cmp_to_key
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def changeNum(num):
            new_num = ""

            while num > 0:
                digit = num % 10
                new_num += str(mapping[digit])
                num //= 10
            
            return int(new_num[::-1]) if new_num else mapping[0]
        
        nums.sort(key=lambda x: changeNum(x))

        return nums