class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = int("".join(map(str, digits)))
        val += 1
        return [int(i) for i in str(val)]