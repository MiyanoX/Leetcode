class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """   
        zero = 0
        while zero < len(nums):
            if nums[zero] == 0:
                break
            else:
                zero += 1
        
        if zero >= len(nums) - 1:
            return
        
        cur = zero + 1
        
        while cur < len(nums):
            if nums[cur] != 0:
                nums[zero], nums[cur] = nums[cur], nums[zero]
                zero += 1
            cur += 1    
        