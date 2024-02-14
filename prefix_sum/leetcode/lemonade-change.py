class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = [0] * 3

        for bill in bills:
            if bill == 5:
                changes[0] += 1
            elif bill == 10:
                if changes[0] >= 1:
                    changes[0] -= 1
                    changes[1] += 1
                else:
                    return False
            elif bill == 20:
                if (changes[0] >= 1 and changes[1] >= 1):
                    changes[0] -= 1
                    changes[1] -= 1
                    changes[2] += 1
                elif changes[0] >= 3:
                    changes[0] -= 3
                    changes[2] += 1
                else:
                    return False
        
        return True
# 
        # 10  0  2