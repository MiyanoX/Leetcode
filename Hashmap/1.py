class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            num = target - nums[i] 
            if num in dict:
                return [dict[num], i]
            else:
                dict[nums[i]] = i