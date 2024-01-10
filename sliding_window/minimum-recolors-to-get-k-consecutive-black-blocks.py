class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        start = 0
        black_count = 0
        min_operation = float('inf')

        for end in range(len(blocks)):
            if blocks[end] == 'B':
                black_count += 1
            
            if (end - start + 1) == k:
                min_operation = min(min_operation, k - black_count)
                if blocks[start] == 'B':
                    black_count -= 1
                
                start += 1
        
        return min_operation if min_operation != float('inf') else 0