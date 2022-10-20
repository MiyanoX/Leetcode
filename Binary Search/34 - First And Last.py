class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        res = [-1, -1]
        first, last = 0, len(nums)-1
        while first <= last:
            i = (first + last) // 2
            if nums[i] == target:
                res[0] = i
                last = i - 1
            elif nums[i] < target:
                first = i + 1
            else:
                last = i - 1
                
        last = len(nums)-1
        while first <= last:
            print(first, last)
            i = (first + last) // 2
            if nums[i] == target:
                res[1] = i
                first = i + 1
            elif nums[i] < target:
                first = i + 1
            else:
                last = i - 1
        
        return res