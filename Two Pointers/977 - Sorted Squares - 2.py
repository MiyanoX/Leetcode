class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        left, right = 0, len(nums) - 1
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                res.append(nums[left] ** 2)
                left += 1
            else:
                res.append(nums[right] ** 2)
                right -= 1
        return res[::-1]