class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-float('inf')] + nums + [-float('inf')]                 # add '-inf' to help edge judgement
        
        start, end = 1, len(nums) - 2                                   # set start and end pointer
        while 0 < start <= end < len(nums) - 1:                         # ensure start < end
            mid = (start + end) // 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:     # if mid num is peak, return mid
                return mid - 1
            elif nums[mid] < nums[mid-1]:                               # if mid num < mid-1 num, search nums[:mid]
                end = mid - 1
            else:                                                       # if mid num < mid+1 num, search nums[mid+1:]
                start = mid + 1