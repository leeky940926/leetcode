from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target :
            return len(nums)
        
        for i in range(len(nums)) :
            if nums[i] >= target :
                return i