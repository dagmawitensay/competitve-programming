class Solution:
    def compress(self, chars: List[str]) -> int:
        check_ptr, write_ptr = 0, 0
        current_char = None
        current_len = 0
        
        while check_ptr < len(chars):
            if chars[check_ptr] != current_char:
                if current_len > 1:
                    char_len = []
                    while current_len > 0:
                        char_len.append(str(current_len % 10))
                        current_len  //= 10
                    
                    for val in char_len[::-1]:
                        chars[write_ptr] = val
                        write_ptr += 1
                    
                chars[write_ptr] = chars[check_ptr]
                write_ptr += 1
                current_char = chars[check_ptr]
                current_len = 1
            else:
                current_len += 1
            
            check_ptr += 1
        
        if current_len > 1:
            char_len = []
            while current_len > 0:
                char_len.append(str(current_len % 10))
                current_len  //= 10

            for val in char_len[::-1]:
                chars[write_ptr] = val
                write_ptr += 1
        
        return write_ptr
        