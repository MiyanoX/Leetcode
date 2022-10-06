class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        min_index = 0
        min_dist = math.inf
        for i in range(len(nums)):
            dist = abs(nums[i])
            if dist < min_dist:
                min_index = i
                min_dist = dist
        
        res = []
        left = min_index
        right = min_index + 1
        while left >= 0 or right < len(nums):
            if left < 0:
                res.append(nums[right] ** 2)
                right += 1
            elif right >= len(nums):
                res.append(nums[left] ** 2)
                left -= 1
            else:
                if abs(nums[left]) <= abs(nums[right]):
                    res.append(nums[left] ** 2)
                    left -= 1
                else:
                    res.append(nums[right] ** 2)
                    right += 1
            # print(left, right, res)
        return res
