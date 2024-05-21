from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        pointer2 = 0
        for pointer1 in range(len_nums):
            num = nums[pointer1]
            if num == 0:
                continue 
            nums[pointer2] = num
            pointer2 += 1
        
        # Line 13 already points to the next
        # so first assign and move  
        while pointer2 < len_nums:
            nums[pointer2] = 0
            pointer2 += 1