class Solution: 
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        nums[1] = max(nums[0:2])
        for i in range(2,len(nums)):
            nums[i] = max(nums[i-1], nums[i-2] + nums[i])
        
        return nums[-1]