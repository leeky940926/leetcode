from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 0 : return 0
        
        k = 1
        idx = 0
        
        while idx < len(nums)-1 :
            if nums[idx] != nums[idx+1] :
                nums[k] = nums[idx+1]
                k+=1
            idx+=1
        
        return k