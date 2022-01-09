from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int: 
        
        max_value = nums[0]
        current_sum = nums[0]
        
        for i in range(1, len(nums)) :
            current_sum = max(nums[i], current_sum+nums[i])
            max_value = max(max_value, current_sum)
            
        return max_value