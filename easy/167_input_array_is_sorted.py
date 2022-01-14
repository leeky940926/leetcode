from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, last = 0, len(numbers)-1
        
        while True :
            if target == numbers[start] + numbers[last] :
                return [start+1, last+1]
            
            elif target > numbers[start] + numbers[last] :
                start += 1
            
            else :
                last -= 1