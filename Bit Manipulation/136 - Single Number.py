class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num # num ^ num = 0, 0 ^ num = num
        return res