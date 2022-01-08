from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        new_str = ''
        new_val = 0
        
        for i in digits :
            new_str += str(i)
        
        return list(str(int(new_str) + 1))